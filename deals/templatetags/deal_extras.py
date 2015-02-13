from django import template
from deals.models import Profile

register = template.Library()

@register.filter
def canUpvoteFormatting(deal, userId):
    if not userId is None:
        if not (deal.canUpvote(userId)):
            return 'disabled'
    
@register.filter
def canDownvoteFormatting(deal, userId):
    if not userId is None:
        if not (deal.canDownvote(userId)):
            return 'disabled'
        
@register.filter
def printSSO(userId):
    if not userId is None:
        aProfile = Profile.objects.get(user=userId)
        return aProfile.get_disqus_sso()