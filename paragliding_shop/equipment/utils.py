from paragliding_shop.equipment.models import Wings


def get_wing_by_name_and_username(wing_slug, username):
    return Wings.objects.get(slug=wing_slug, user__username=username)