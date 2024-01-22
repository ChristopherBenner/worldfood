# badges/functions.py
from .models import AwardedBadge, Badge, BadgeCategory
from notifications.models import Notification
def add_badge(user, badge_category, points):
    '''
    For a given user, go through each badge in a
    specified badge_category. If the earned points are greater than
    or equal to the points required, award the badge.
    '''
    badges = Badge.objects.filter(badge_category__category__contains  = badge_category)
    for badge in badges:
        if points >= badge.points_required:
            awarded_badge, created = AwardedBadge.objects.get_or_create(badge = badge, awarded_to = user)
            if created:
                Notification.objects.create(
                    category = "badge awarded",
                    description = badge.badge_name + ' badge awarded',
                    user = user
                )
