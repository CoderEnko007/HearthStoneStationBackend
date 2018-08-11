import xadmin
from xadmin import views

class GlobalSetting(object):
    # site_header = '炉石传说情报站后台'
    site_title = '炉石传说情报站管理系统'
    site_footer = '炉石传说情报站后台'
    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)