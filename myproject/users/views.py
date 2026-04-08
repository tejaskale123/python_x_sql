from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
# ================= REGISTER =================
def register(request):
    if request.method == "POST":
        username = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not email or not password:
            return render(request, "register.html", {"error": "All fields are required."})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists."})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already exists."})

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, "register.html")


# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        login_input = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        user = authenticate(request, username=login_input, password=password)

        # If login using email
        if not user:
            try:
                user_obj = User.objects.get(email=login_input)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        if user:
            login(request, user)
            return redirect('dashboard')

        return render(request, "login.html", {"error": "Invalid login credentials."})

    return render(request, "login.html")


# ================= DASHBOARD =================
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "dashboard.html", {"user": request.user})


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('login')


# ================= USERS LIST =================
def users_list(request):
    try:
        users = User.objects.filter(is_superuser=False).order_by('username')
    except Exception as e:
        messages.error(request, f"Error loading users: {str(e)}")
        users = []

    return render(request, "users.html", {"users": users})


# ================= DELETE USER =================
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, f"User '{user.username}' deleted successfully!")
    except User.DoesNotExist:
        messages.error(request, "User not found!")
    except Exception as e:
        messages.error(request, f"Error deleting user: {str(e)}")

    return redirect('users')


# ================= UPDATE USER =================
def update_user(request, id):
    try:
        user = User.objects.get(id=id)

        if request.method == "POST":
            username = request.POST.get("name", "").strip()
            email = request.POST.get("email", "").strip()

            if not username or not email:
                messages.error(request, "Name and email are required!")
                return redirect('update', id=id)

            if User.objects.filter(username=username).exclude(id=id).exists():
                messages.error(request, "Username already exists.")
                return redirect('update', id=id)

            if User.objects.filter(email=email).exclude(id=id).exists():
                messages.error(request, "Email already exists.")
                return redirect('update', id=id)

            user.username = username
            user.email = email
            user.save()
            messages.success(request, "User updated successfully!")
            return redirect('users')

    except User.DoesNotExist:
        messages.error(request, "User not found!")
        return redirect('users')
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect('users')

    return render(request, "update.html", {"user": user})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "profile.html", {"user": request.user})


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        new_password = request.POST.get("password", "").strip()

        if not new_password or len(new_password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect('change_password')

        user = request.user
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Password updated successfully.")
        return redirect('dashboard')

    return render(request, "change_password.html")
    
# ================= GET ALL USERS =================
@api_view(['GET'])
def api_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

    # ================= CREATE USER (POST) =================
@api_view(['POST'])
def api_create_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"})

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({
        "message": "User created",
        "id": user.id
    })


# ================= UPDATE USER =================
@api_view(['PUT'])
def api_update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"})

    user.username = request.data.get('username', user.username)
    user.email = request.data.get('email', user.email)
    user.save()

    return Response({"message": "User updated"})


# ================= DELETE USER =================
@api_view(['DELETE'])
def api_delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response({"message": "User deleted"})
    except User.DoesNotExist:
        return Response({"error": "User not found"})

# ================= LOGIN (API) =================#
@api_view(['POST'])
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "message": "Login success",
            "user_id": user.id
        })
    else:
        return Response({"error": "Invalid credentials"})