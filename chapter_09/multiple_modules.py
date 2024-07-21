import privileges_module as permissions

admin = permissions.Admin("admin", "administrator", 0)
admin.privileges.show_privileges()
