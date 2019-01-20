def active_menu(request):
    path = request.path.split("/")
    active = None
    if 'users' in path:
        active = 'users'
    elif 'statistics' in path:
        active = 'statistics'
    else:
        active = "home"

    return {'menu': active}