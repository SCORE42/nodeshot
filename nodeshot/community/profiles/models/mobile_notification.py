#from django.db import models
#from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
#
#from nodeshot.core.base.models import BaseDate
#
#
#class MobileNotification(models.Model):
#    """
#    User Mobile Notification Model
#    Takes care of tracking the user's mobile notification preferences
#    """
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'))
#    # TODO
#    # this is not on schedule yet... here just as a reminder.. hold on
#    
#    class Meta:
#        db_table = 'profile_mobile_notification'
#        app_label= 'profiles'
