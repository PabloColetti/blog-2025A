from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.post.models import Post, Comment
from apps.user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            post_content_type = ContentType.objects.get_for_model(Post)
            comment_content_type = ContentType.objects.get_for_model(Comment)

            # Permisos de POST
            view_post_permission = Permission.objects.get(
                codename='view_post', content_type=post_content_type)
            add_post_permission = Permission.objects.get(
                codename='add_post', content_type=post_content_type)
            change_post_permission = Permission.objects.get(
                codename='change_post', content_type=post_content_type)
            delete_post_permission = Permission.objects.get(
                codename='delete_post', content_type=post_content_type)

            # Permisos de COMMENT
            view_comment_permission = Permission.objects.get(
                codename='view_comment', content_type=comment_content_type)
            add_comment_permission = Permission.objects.get(
                codename='add_comment', content_type=comment_content_type)
            change_comment_permission = Permission.objects.get(
                codename='change_comment', content_type=comment_content_type)
            delete_comment_permission = Permission.objects.get(
                codename='delete_comment', content_type=comment_content_type)

            # Crear grupos de usuarios registrados
            registered_group, created = Group.objects.get_or_create(
                name="Registered"
            )
            registered_group.permissions.add(
                view_post_permission,
                view_comment_permission,
                add_comment_permission,
                change_comment_permission,
                delete_comment_permission,
                # permiso para ver post
                # permiso para ver comentarios del post
                # permiso para crear comentarios del post
                # permiso para actualizar de su comentario en un post
                # permiso para borrar su comentario en un post
            )

            # Crear grupos de usuarios colaboradores
            registered_group, created = Group.objects.get_or_create(
                name="Collaborators"
            )
            registered_group.permissions.add(
                view_post_permission,
                add_post_permission,
                change_post_permission,
                delete_post_permission,
                view_comment_permission,
                add_comment_permission,
                change_comment_permission,
                delete_comment_permission,
                # permiso para ver post
                # permiso para crear post
                # permiso para actualizar su post
                # permiso para borrar su post
                # permiso para ver comentarios del post
                # permiso para crear comentarios del post
                # permiso para actualizar de su comentario en un post
                # permiso para borrar su comentario en un post
            )

            # Crear grupos de usuarios administradores
            registered_group, created = Group.objects.get_or_create(
                name="Admins"
            )
            registered_group.permissions.add(
                view_post_permission,
                add_post_permission,
                change_post_permission,
                delete_post_permission,
                view_comment_permission,
                add_comment_permission,
                change_comment_permission,
                delete_comment_permission,
                # permiso para ver post
                # permiso para crear post
                # permiso para actualizar su post
                # permiso para borrar cualquier post
                # permiso para ver comentarios del post
                # permiso para crear comentarios del post
                # permiso para actualizar de su comentario en un post
                # permiso para borrar su comentario de cualquier post
            )

            print("Grupos y Permisos creados exitosamente.")
        except ContentType.DoesNotExist:
            print("El tipo aun no se encuentra disponible.")
        except Permission.DoesNotExist:
            print("Uno o mas permisos no se encuentran disponibles")
