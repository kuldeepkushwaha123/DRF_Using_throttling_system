from rest_framework.throttling import UserRateThrottle

class UserThrottle(UserRateThrottle):
    scope = "for_user"