# badges/functions.py
from .models import AwardedBadge, Badge, BadgeCategory

def add_badge(user, badge_category, points):
    '''
    For a given user, go through each badge in a
    specified badge_category. If the earned points are greater than
    or equal to the points required, award the badge.
    '''
    # category = BadgeCategory.objects.filter(category__contains = badge_category).first
    badges = Badge.objects.filter(badge_category__category__contains  = badge_category)
    for badge in badges:
        print(badge.points_required)
        if points >= badge.points_required:
            awarded_badge = AwardedBadge(badge = badge, awarded_to = user)
            awarded_badge.save()
