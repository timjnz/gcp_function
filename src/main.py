import functions_framework

@functions_framework.http
def slugify(request):
    if request.method == "POST":
        name = request.get_json.get('name', 'World')
        return f"Success: your name is now {name}!"
    name = request.args.get('name', 'World')
    return f"Hello {name}"
