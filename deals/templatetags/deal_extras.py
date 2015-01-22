from django import template

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