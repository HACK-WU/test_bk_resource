# -*- coding: utf-8 -*-

from bk_resource.routers import ResourceRouter
from app0 import views

router = ResourceRouter()
router.register_module(views)

urlpatterns = router.urls
print("urlpatterns:", urlpatterns)
