from rest_framework.permissions import BasePermission
from datetime import date

class IsOwnerOrStaff(BasePermission):
	message = "You don't have access."

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (request.user == obj.user):
			return True
		return False

class DaysLimit(BasePermission):
	message = "You don't have permission."

	def has_object_permission(self, request, view, obj):
		# print("---------------------------")
		# print(((obj.date - date.today()).days) > 3)
		# print(((obj.date - date.today()).days))
		# print("^v")
		# print(((date.today() - obj.date).days))
		# print(((date.today() - obj.date).days) <= 3)
		# print("---------------------------")
		if (obj.date - date.today()).days > 3:
			return True
		return False