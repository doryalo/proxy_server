from rest_framework.throttling import AnonRateThrottle


class DayAnonThrottle(AnonRateThrottle):
    scope = 'anon_day'
    THROTTLE_RATES = {
        'anon_day': '1000/day'
    }


class MinuteAnonThrottle(AnonRateThrottle):
    scope = 'anon_min'
    THROTTLE_RATES = {
        'anon_min': '10/minute'
    }