""" REST views for the Persistent Query Periodic Table.
"""

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
)
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core_main_app.access_control.exceptions import AccessControlError
from core_main_app.commons import exceptions
import core_explore_periodic_table_app.components.persistent_query_periodic_table.api as persistent_query_periodic_table_api
from core_explore_periodic_table_app.rest.persistent_query_periodic_table.serializers import (
    PersistentQueryPeriodicTableSerializer,
    PersistentQueryPeriodicTableAdminSerializer,
)


@extend_schema(
    tags=["Admin Persistent Query by Periodic Table"],
    description="List all persistent query by periodic table, or create a new one.",
)
class AdminPersistentQueryPeriodicTableList(APIView):
    """List all persistent query by periodic table, or create a new one."""

    permission_classes = (IsAdminUser,)
    serializer = PersistentQueryPeriodicTableAdminSerializer

    @extend_schema(
        summary="Get all persistent query by periodic table",
        description="Get all user persistent query by periodic table",
        responses={
            200: PersistentQueryPeriodicTableAdminSerializer(many=True),
            403: OpenApiResponse(description="Access Forbidden"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def get(self, request):
        """Get all user persistent query by periodic table
        Args:
            request: HTTP request
        Returns:
            - code: 200
              content: List of persistent query by periodic table
            - code: 403
              content: Forbidden
            - code: 500
              content: Internal server error
        """
        if not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            # Get object
            object_list = persistent_query_periodic_table_api.get_all(
                request.user
            )
            # Serialize object
            serializer = self.serializer(object_list, many=True)
            # Return response
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Create a new persistent query by periodic table",
        description="Create a persistent query by periodic table",
        request=PersistentQueryPeriodicTableAdminSerializer,
        responses={
            201: PersistentQueryPeriodicTableAdminSerializer,
            400: OpenApiResponse(description="Validation error"),
            403: OpenApiResponse(description="Access Forbidden"),
            500: OpenApiResponse(description="Internal server error"),
        },
        examples=[
            OpenApiExample(
                "Example request",
                summary="Example request body",
                description="Example request body for creating a persistent query by periodic table",
                value={
                    "content": "{}",
                    "templates": ["123"],
                    "name": "persistent_query_periodic_table",
                },
            ),
        ],
    )
    def post(self, request):
        """Create a persistent query by periodic table
        Parameters:
            {
              "content": "{}",
              "templates": ["123"],
              "name": "persistent_query_periodic_table"
            }
        Args:
            request: HTTP request
        Returns:
            - code: 201
              content: Created persistent query by periodic table
            - code: 400
              content: Validation error
            - code: 403
              content: Forbidden
            - code: 500
              content: Internal server error
        """
        if not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        try:
            # Build serializer
            serializer = self.serializer(
                data=request.data, context={"request": request}
            )
            # Validate data
            serializer.is_valid(raise_exception=True)
            # Save data
            serializer.save()
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as validation_exception:
            content = {"message": validation_exception.detail}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(
    tags=["Persistent Query by Periodic Table"],
    description="List all persistent query by periodic table or create one",
)
class PersistentQueryPeriodicTableList(APIView):
    """List all persistent query by periodic table or create one"""

    permission_classes = (IsAuthenticated,)
    serializer = PersistentQueryPeriodicTableSerializer

    @extend_schema(
        summary="Get all user persistent query by periodic table",
        description="Get all user persistent query by periodic table",
        responses={
            200: PersistentQueryPeriodicTableSerializer(many=True),
            403: OpenApiResponse(description="Access Forbidden"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def get(self, request):
        """Get all user persistent query by periodic table
        Args:
            request: HTTP request
        Returns:
            - code: 200
              content: List of persistent query by periodic table
            - code: 403
              content: Forbidden
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            object_list = persistent_query_periodic_table_api.get_all_by_user(
                request.user
            )
            # Serialize object
            serializer = self.serializer(object_list, many=True)
            # Return response
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Create a new persistent query by periodic table",
        description="Create a new persistent query by periodic table",
        request=PersistentQueryPeriodicTableSerializer,
        responses={
            201: PersistentQueryPeriodicTableSerializer,
            400: OpenApiResponse(description="Validation error"),
            500: OpenApiResponse(description="Internal server error"),
        },
        examples=[
            OpenApiExample(
                "Example request",
                summary="Example request body",
                description="Example request body for creating a persistent query by periodic table",
                value={
                    "content": "{}",
                    "templates": ["123"],
                    "name": "persistent_query_periodic_table",
                },
            ),
        ],
    )
    def post(self, request):
        """Create a new persistent query by periodic table
        Parameters:
            {
              "content": "{}",
              "templates": ["123"],
              "name": "persistent_query_periodic_table"
            }
        Args:
            request: HTTP request
        Returns:
            - code: 201
              content: Created data
            - code: 400
              content: Validation error
            - code: 500
              content: Internal server error
        """
        try:
            # Build serializer
            serializer = self.serializer(
                data=request.data, context={"request": request}
            )
            # Validate data
            serializer.is_valid(raise_exception=True)
            # Save data
            serializer.save()
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as validation_exception:
            content = {"message": validation_exception.detail}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(
    tags=["Persistent Query by Periodic Table"],
    description="Persistent query by periodic table detail",
)
class PersistentQueryPeriodicTableDetail(APIView):
    """Persistent query by periodic table detail"""

    permission_classes = (IsAuthenticated,)
    serializer = PersistentQueryPeriodicTableSerializer

    @extend_schema(
        summary="Retrieve a persistent query by periodic table",
        description="Retrieve persistent query by periodic table from database",
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.PATH,
                description="Persistent query by periodic table ID",
            ),
        ],
        responses={
            200: PersistentQueryPeriodicTableSerializer,
            403: OpenApiResponse(description="Access Forbidden"),
            404: OpenApiResponse(description="Object was not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def get(self, request, pk):
        """Retrieve persistent query by periodic table from database
        Args:
            request: HTTP request
            pk: ObjectId
        Returns:
            - code: 200
              content: persistent query by periodic table
            - code: 403
              content: Forbidden
            - code: 404
              content: Object was not found
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            persistent_query_periodic_table = (
                persistent_query_periodic_table_api.get_by_id(pk, request.user)
            )
            # Serialize object
            serializer = self.serializer(persistent_query_periodic_table)
            # Return response
            return Response(serializer.data)
        except exceptions.DoesNotExist:
            content = {"message": "Object not found."}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Update a persistent query by periodic table",
        description="Update a persistent query by periodic table",
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.PATH,
                description="Persistent query by periodic table ID",
            ),
        ],
        request=PersistentQueryPeriodicTableSerializer,
        responses={
            200: PersistentQueryPeriodicTableSerializer,
            400: OpenApiResponse(description="Validation error"),
            403: OpenApiResponse(description="Access Forbidden"),
            404: OpenApiResponse(description="Object was not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
        examples=[
            OpenApiExample(
                "Example request",
                summary="Example request body",
                description="Example request body for updating a persistent query by periodic table",
                value={
                    "content": "{}",
                    "templates": ["123"],
                    "name": None,
                },
            ),
        ],
    )
    def patch(self, request, pk):
        """Update a persistent query by periodic table
        Parameters:
            {
              "content": "{}",
              "templates": ["123"],
              "name": null
            }
        Args:
            request: HTTP request
            pk: ObjectId
        Returns:
            - code: 200
              content: Updated data
            - code: 400
              content: Validation error
            - code: 403
              content: Forbidden
            - code: 404
              content: Object was not found
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            persistent_query_periodic_table = (
                persistent_query_periodic_table_api.get_by_id(pk, request.user)
            )
            # Build serializer
            serializer = self.serializer(
                instance=persistent_query_periodic_table,
                data=request.data,
                partial=True,
                context={"request": request},
            )
            # Validate and save persistent query periodic table
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as validation_exception:
            content = {"message": validation_exception.detail}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except exceptions.NotUniqueError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.DoesNotExist:
            content = {"message": "Persistent query periodic table not found."}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Delete a persistent query by periodic table",
        description="Delete a persistent query by periodic table",
        parameters=[
            OpenApiParameter(
                name="id",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.PATH,
                description="Persistent query by periodic table ID",
            ),
        ],
        responses={
            204: None,
            403: OpenApiResponse(description="Access Forbidden"),
            404: OpenApiResponse(description="Object was not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def delete(self, request, pk):
        """Delete a persistent query periodic table
        Args:
            request: HTTP request
            pk: ObjectId
        Returns:
            - code: 204
              content: Deletion success
            - code: 403
              content: Authentication error
            - code: 404
              content: Object was not found
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            persistent_query_periodic_table = (
                persistent_query_periodic_table_api.get_by_id(pk, request.user)
            )
            # delete object
            persistent_query_periodic_table_api.delete(
                persistent_query_periodic_table, request.user
            )
            # Return response
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except exceptions.DoesNotExist:
            content = {
                "message": "Persistent query by periodic table not found."
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(
    tags=["Persistent Query by Periodic Table"],
    description="Persistent query by periodic table detail",
)
class PersistentQueryPeriodicTableByName(APIView):
    """Persistent query by periodic table detail"""

    permission_classes = (IsAuthenticated,)
    serializer = PersistentQueryPeriodicTableSerializer

    @extend_schema(
        summary="Retrieve a persistent query by periodic table by name",
        description="Retrieve persistent query by periodic table from database",
        parameters=[
            OpenApiParameter(
                name="name",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.PATH,
                description="Persistent query by periodic table name",
            ),
        ],
        responses={
            200: PersistentQueryPeriodicTableSerializer,
            403: OpenApiResponse(description="Access Forbidden"),
            404: OpenApiResponse(description="Object was not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
    )
    def get(self, request, name):
        """Retrieve persistent query by periodic table from database
        Args:
            request: HTTP request
            name: name
        Returns:
            - code: 200
              content: persistent query by periodic table
            - code: 403
              content: Forbidden
            - code: 404
              content: Object was not found
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            persistent_query_periodic_table = (
                persistent_query_periodic_table_api.get_by_name(
                    name, request.user
                )
            )
            # Serialize object
            serializer = self.serializer(persistent_query_periodic_table)
            # Return response
            return Response(serializer.data)
        except exceptions.DoesNotExist:
            content = {
                "message": "Persistent query by periodic table not found."
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except AccessControlError as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(
                content, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
