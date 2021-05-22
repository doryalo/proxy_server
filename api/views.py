from celery.result import AsyncResult
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.mixins import ListModelMixin
from django.contrib.auth import authenticate, login
from django.core.cache import caches
import requests
# Create your views here.
from api.tasks import get_users_list
from common.constants import TASK_STATUS_SUCCESS
from common.throttling import DayAnonThrottle, MinuteAnonThrottle
from config.celery import app as celery_app
from common.exceptions import MissingTaskIDError


class UsersView(ViewSet, ListModelMixin):
    throttle_classes = [MinuteAnonThrottle, DayAnonThrottle]

    def list(self, request, *args, **kwargs):
        task_id = request.query_params.get('task_id', None)
        if task_id is None:
            raise MissingTaskIDError
        task = AsyncResult(task_id, app=celery_app)
        if task.state == TASK_STATUS_SUCCESS:
            return Response(task.get())
        else:
            return Response({'task_id': task.id, 'status': task.state})

    @action(detail=False)
    def initiate_users_list_task(self, request, *args, **kwargs):
        task = get_users_list.delay()
        return Response({'task_id': task.id, 'status': task.status})
