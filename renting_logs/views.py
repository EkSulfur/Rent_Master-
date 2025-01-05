from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Admin, Tenant, House
from django.urls import reverse
from django.contrib import messages
from .sendemail import send_email

key = "666"  # 定义管理员密钥

# 主页视图
def home(request):
    return render(request, 'home.html')


def admin_home(request):
    try:
        admin_id = request.session.get('admin_id')
        admin = Admin.objects.get(id=admin_id)
        # 在这里可以使用admin对象来渲染特定管理员的主页内容
        return render(request, 'admin_home.html', {'admin': admin})
    except Admin.DoesNotExist:
        return render(request, 'admin_home.html', {'error': '管理员不存在'})


def tenant_home(request):
    try:
        tenant_id = request.session.get('tenant_id')
        tenant = Tenant.objects.get(id=tenant_id)
        # 在这里可以使用admin对象来渲染特定管理员的主页内容
        return render(request, 'tenant_home.html', {'tenant': tenant})
    except Tenant.DoesNotExist:
        return render(request, 'tenant_home.html', {'error': '租户不存在'})


def edit_tenant_info(request):
    # 获取当前登录用户的ID（假设已设置在会话中）
    tenant_id = request.session.get('tenant_id')
    if not tenant_id:
        return redirect('login_tenant')
    try:
        tenant = Tenant.objects.get(id=tenant_id)
    except Tenant.DoesNotExist:
        return render(request, 'edit_tenant_info.html', {'error': '租户不存在'})
    if request.method == "POST":
        email = request.POST.get('email')

        if Tenant.objects.filter(email=email).exists() and email != tenant.email:
            # 重定向回注册页面并附加查询参数
            return render(request, 'edit_tenant_info.html', {'error': '邮箱已占用', 'tenant': tenant})

        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        tenant.full_name = full_name
        tenant.phone_number = phone_number
        tenant.email = email
        tenant.gender = gender
        tenant.save()
        return redirect('tenant_home')
    else:
        return render(request, 'edit_tenant_info.html', {'tenant': tenant})


def edit_tenant_password(request):
    # 获取当前登录用户的ID（假设已设置在会话中）
    tenant_id = request.session.get('tenant_id')
    if not tenant_id:
        return redirect('login_tenant')
    try:
        tenant = Tenant.objects.get(id=tenant_id)
    except Tenant.DoesNotExist:
        return render(request, 'edit_tenant_password.html', {'error': '租户不存在'})
    if request.method == "POST":
        username = request.POST.get('new_username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if Tenant.objects.filter(username=username).exists() and username != tenant.username:
            # 重定向回注册页面并附加查询参数
            return render(request, 'edit_tenant_password.html', {'error': '用户名已占用', 'tenant': tenant})

        # 验证原密码是否正确
        if not check_password(old_password, tenant.password):
            return render(request, 'edit_tenant_password.html', {'error': '原密码不正确', 'tenant': tenant})
        # 验证新密码是否匹配
        if new_password != confirm_password:
            return render(request, 'edit_tenant_password.html', {'error': '新密码不匹配', 'tenant': tenant})
        # 更新用户信息
        tenant.username = username
        tenant.password = make_password(new_password)
        tenant.save()
        return redirect('tenant_home')
    else:
        return render(request, 'edit_tenant_password.html', {'tenant': tenant})


def edit_admin_info(request):
    # 获取当前登录用户的ID（假设已设置在会话中）
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('login_admin')
    try:
        admin = Admin.objects.get(id=admin_id)
    except Admin.DoesNotExist:
        return render(request, 'edit_admin_info.html', {'error': '管理员不存在'})
    if request.method == "POST":
        username = request.POST.get('new_username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if Admin.objects.filter(username=username).exists() and username != admin.username:
            # 重定向回注册页面并附加查询参数
            return render(request, 'edit_admin_info.html', {'error': '用户名已占用', 'admin': admin})

        # 验证原密码是否正确
        if not check_password(old_password, admin.password):
            return render(request, 'edit_admin_info.html', {'error': '原密码不正确', 'admin': admin})
        # 验证新密码是否匹配
        if new_password != confirm_password:
            return render(request, 'edit_admin_info.html', {'error': '新密码不匹配', 'admin': admin})
        # 更新用户名和密码
        admin.username = username
        admin.password = make_password(new_password)
        admin.save()
        return redirect('admin_home')
    else:
        return render(request, 'edit_admin_info.html', {'admin': admin})


def add_house(request):
    message = ''  # 用于展示操作成功的消息
    if request.method == 'POST':
        house_number = request.POST.get('house_number')
        area = request.POST.get('area')
        location = request.POST.get('location')
        layout = request.POST.get('layout')
        monthly_rent = request.POST.get('monthly_rent')
        status = request.POST.get('status')

        House.objects.create(
            house_number=house_number,
            area=area,
            location=location,
            layout=layout,
            monthly_rent=monthly_rent,
            status=status
        )

        message = '房屋信息已成功添加！'  # 设置成功消息

    context = {
        'message': message
    }
    return render(request, 'add_house.html', context)


def view_houses(request):
    houses = House.objects.all()  # 获取所有房屋信息

    # 如果是POST请求，处理房屋信息的更新
    if request.method == 'POST':
        house_id = request.POST.get('house_id')
        house = House.objects.get(id=house_id)

        house.house_number = request.POST.get('house_number')
        house.area = request.POST.get('area')
        house.location = request.POST.get('location')
        house.layout = request.POST.get('layout')
        house.monthly_rent = request.POST.get('monthly_rent')
        house.status = request.POST.get('status')

        house.save()

        return redirect('view_houses')  # 重定向到房屋管理页面

    return render(request, 'view_houses.html', {'houses': houses})


def search_and_rent(request):
    houses = House.objects.all()  # 初始查询获取所有房屋

    # 处理搜索查询
    if request.method == 'GET' and 'search' in request.GET:
        query = request.GET
        status = query.get('status')

        if status == 'available':
            houses = houses.filter(status='可出租')
        elif status == 'unavailable':
            houses = houses.filter(status='不可出租')

        min_area = query.get('min_area')
        max_area = query.get('max_area')

        if min_area:
            houses = houses.filter(area__gte=min_area)

        if max_area:
            houses = houses.filter(area__lte=max_area)

        if query.get('location'):
            houses = houses.filter(location__icontains=query['location'])

        if query.get('layout'):
            houses = houses.filter(layout=query['layout'])

        min_rent = query.get('min_rent')
        max_rent = query.get('max_rent')

        if min_rent:
            houses = houses.filter(monthly_rent__gte=min_rent)

        if max_rent:
            houses = houses.filter(monthly_rent__lte=max_rent)

    context = {'houses': houses}

    # 处理租房请求
    if request.method == 'POST' and 'rent_house' in request.POST:
        house_id = request.POST.get('house_id')
        rent_duration = request.POST.get('rent_duration', 1)  # 默认租赁时间为1个月

        if rent_duration == '':
            context['error'] = '请输入租赁日期。'
            return render(request, 'search_and_rent.html', context)

        rent_duration = int(rent_duration)

        try:
            selected_house = House.objects.get(id=house_id)
            cost = selected_house.monthly_rent * rent_duration
            fee = cost * 0.10  # 假设手续费为租金的10%
            total_cost = cost + fee
            context.update({
                'selected_house': selected_house,
                'cost': cost,
                'fee': fee,
                'total_cost': total_cost,
                'selected_rent_duration': rent_duration
            })

            request.session['selected_house_info'] = {
                'house_number': selected_house.house_number,
                'location': selected_house.location,
                'monthly_rent': selected_house.monthly_rent,
                'cost': cost,
                'fee': fee,
                'total_cost': total_cost,
                'rent_duration': rent_duration
            }

            return render(request, 'rent_confirmation.html', context)
        except House.DoesNotExist:
            # 处理房屋不存在的情况
            context['error'] = '选择的房屋不存在。'
        except ValueError:
            # 处理数据类型转换错误的情况
            context['error'] = '无效的输入。'

    return render(request, 'search_and_rent.html', context)


def rent_confirmation(request):
    if request.method == 'POST' and 'send_email' in request.POST:
        tenant_id = request.session.get('tenant_id')
        tenant = Tenant.objects.get(id=tenant_id)
        if tenant and tenant.email:
            selected_house_info = request.session.get('selected_house_info', {})
            email_content = f"租房信息：\n房屋编号：{selected_house_info.get('house_number')}\n位置：{selected_house_info.get('location')}\n月租金：{selected_house_info.get('monthly_rent')}元\n总费用：{selected_house_info.get('total_cost')}元\n租赁时间：{selected_house_info.get('rent_duration')}个月"
            send_email(tenant, email_content)
            messages.success(request, '邮件发送成功！')

        else:
            messages.error(request, '邮件发送失败！')
    return render(request, 'rent_confirmation.html')


def manage_houses(request):
    # 如果是POST请求，则处理状态更新或房屋删除
    if request.method == 'POST':
        selected_houses = request.POST.getlist('selected_houses')
        action = request.POST['action']

        if action == 'update_status':
            new_status = request.POST['status_update']
            # 更新选中房屋的状态
            House.objects.filter(id__in=selected_houses).update(status=new_status)
        elif action == 'delete':
            # 删除选中的房屋
            House.objects.filter(id__in=selected_houses).delete()

        return redirect('manage_houses')  # 重定向以查看更新后的房屋列表

    # 获取查询参数
    status = request.GET.get('status')

    if status:
        # 如果提供了状态参数，则筛选房屋
        houses = House.objects.filter(status=status)
    else:
        # 否则，获取所有房屋信息
        houses = House.objects.all()

    return render(request, 'manage_houses.html', {'houses': houses})


def edit_tenant_password_admin(request):
    tenant_id = request.session.get('tenant_id')
    if not tenant_id:
        return redirect('admin_edit_tenant')
    try:
        tenant = Tenant.objects.get(id=tenant_id)
    except Tenant.DoesNotExist:
        return render(request, 'admin_edit_tenant.html', {'error': '租户不存在'})
    if request.method == "POST":
        username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if Tenant.objects.filter(username=username).exists() and username != tenant.username:
            # 重定向回注册页面并附加查询参数
            return render(request, 'edit_tenant_password_admin.html', {'error': '用户名已占用', 'tenant': tenant})

        # 验证新密码是否匹配
        if new_password != confirm_password:
            return render(request, 'edit_tenant_password_admin.html', {'error': '新密码不匹配', 'tenant': tenant})
        email = request.POST.get('email')
        if Tenant.objects.filter(email=email).exists() and email != tenant.email:
            # 重定向回注册页面并附加查询参数
            return render(request, 'edit_tenant_password_admin.html', {'error': '邮箱已占用', 'tenant': tenant})
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        tenant.full_name = full_name
        tenant.phone_number = phone_number
        tenant.email = email
        tenant.gender = gender
        tenant.username = username
        tenant.password = make_password(new_password)
        tenant.save()
        return redirect('admin_edit_tenant')
    else:
        return render(request, 'edit_tenant_password_admin.html', {'tenant': tenant})


def admin_edit_tenant(request):
    if request.method == 'POST':
        selected_tenants = request.POST.getlist('selected_tenants')
        action = request.POST['action']

        if action == 'update_status':
            tenant = Tenant.objects.get(id__in=selected_tenants)
            request.session['tenant_id'] = tenant.id  # 设置会话数据
            return render(request, 'edit_tenant_password_admin.html', {'tenant': tenant})
        elif action == 'delete':
            # 删除选中的房屋
            Tenant.objects.filter(id__in=selected_tenants).delete()

        return redirect('admin_edit_tenant')  # 重定向以查看更新后的房屋列表
    tenants = Tenant.objects.all()

    return render(request, 'admin_edit_tenant.html', {'tenants': tenants})


# 管理员登录视图
def login_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(username=username)
            if check_password(password, admin.password):
                # 登录成功逻辑，例如设置session
                request.session['admin_id'] = admin.id  # 设置会话数据
                return redirect('admin_home')
            else:
                return render(request, 'login_admin.html', {'error': '密码错误'})
        except Admin.DoesNotExist:
            return render(request, 'login_admin.html', {'error': '用户名不存在'})
    else:
        return render(request, 'login_admin.html')


# 管理员注册视图
def register_admin(request):
    context = {'admin_key': key}
    if request.method == "POST":
        username = request.POST.get('username')

        if Admin.objects.filter(username=username).exists():
            # 重定向回注册页面并附加查询参数
            return redirect(reverse('register_admin') + '?username_taken=true')

        password = make_password(request.POST.get('password'))
        Admin.objects.create(username=username, password=password)
        return redirect('login_admin')
    else:
        return render(request, 'register_admin.html', context)


# 租户登录视图
def login_tenant(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            tenant = Tenant.objects.get(username=username)
            if check_password(password, tenant.password):
                # 登录成功逻辑，例如设置session
                request.session['tenant_id'] = tenant.id  # 设置会话数据
                return redirect('tenant_home')  # 重定向到租户的主页或其他适当页面
            else:
                return render(request, 'login_tenant.html', {'error': '密码错误'})
        except Tenant.DoesNotExist:
            return render(request, 'login_tenant.html', {'error': '用户名不存在'})
    else:
        return render(request, 'login_tenant.html')


# 租户注册视图
def register_tenant(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        email = request.POST.get('email')

        if Tenant.objects.filter(username=username).exists():
            # 重定向回注册页面并附加查询参数
            return redirect(reverse('register_tenant') + '?username_taken=true')
        if Tenant.objects.filter(email=email).exists():
            # 重定向回注册页面并附加查询参数
            return redirect(reverse('register_tenant') + '?email_taken=true')

        Tenant.objects.create(
            username=username, password=password,
            email=email
        )
        return redirect('login_tenant')
    else:
        return render(request, 'register_tenant.html')
