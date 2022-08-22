""" REST views for the Search operators Mapping API
"""

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from core_main_app.commons import exceptions
from core_explore_periodic_table_app.components.search_operator_mapping import (
    api as search_operator_mapping_api,
)
from core_explore_periodic_table_app.rest.search_operator_mapping.serializers import (
    SearchOperatorMappingSerializer,
)


class SearchOperatorsMapping(APIView):
    """List the Search Operators Mapping."""

    permission_classes = (IsAdminUser,)
    serializer = SearchOperatorMappingSerializer

    def get(self, request):
        """Get all the search operator mapping object

        Url Parameters:

        Examples:

            ../search-operators-mapping/

        Args:

            request: HTTP request

        Returns:

            - code: 200
              content: List of search operator mapping
            - code: 500
              content: Internal server error
        """
        try:

            # Get objects
            search_operator_mapping_object_list = search_operator_mapping_api.get_all()

            # Serialize object
            search_operator_mapping_serializer = self.serializer(
                search_operator_mapping_object_list, many=True
            )

            # Return response
            return Response(
                search_operator_mapping_serializer.data, status=status.HTTP_200_OK
            )
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """Create a search operator mapping

        Url Parameters:

        Examples:

            ../search-operators-mapping/

        Args:

            request: HTTP request

        Returns:

                - code: 201
                  content: Created search operator
                - code: 400
                  content: Validation error / not unique / model error
                - code: 404
                  content: Search operator not found
                - code: 500
                  content: Internal server error
        """
        try:

            # Build serializer
            serializer = SearchOperatorMappingSerializer(data=request.data)

            # Validate data
            serializer.is_valid(True)

            # Save data
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as validation_exception:
            content = {"message": validation_exception.detail}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.DoesNotExist as does_not_exist_exception:
            content = {"message": str(does_not_exist_exception)}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except exceptions.NotUniqueError as not_unique_error:
            content = {"message": str(not_unique_error)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as key_error:
            content = {"message": str(key_error)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.ApiError as api_exception:
            content = {"message": str(api_exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as exception:
            content = {"message": str(exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchOperatorMappingDetail(APIView):
    """Search operator mapping detail"""

    permission_classes = (IsAdminUser,)
    serializer = SearchOperatorMappingSerializer

    def get(self, request, pk):
        """Retrieve search operator mapping from database

        Args:

            request: HTTP request
            pk: ObjectId

        Returns:
            SearchOperatorMapping object
        """
        try:
            # Get object
            search_operator_mapping = search_operator_mapping_api.get_by_id(pk=pk)

            # Serialize object
            serializer = SearchOperatorMappingSerializer(search_operator_mapping)

            # Return response
            return Response(serializer.data)
        except exceptions.DoesNotExist:
            content = {"message": "Search operator mapping not found."}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        """Update a search operator mapping

        Parameters:
            {
                "search_operator_id": <search_operator_id>
            }

        Args:
            request: HTTP request
            pk: ObjectId

        Returns:
            - code: 200
              content: Updated data
            - code: 400
              content: Validation error
            - code: 404
              content: Object was not found
            - code: 500
              content: Internal server error
        """
        try:
            # Get object
            search_operator_mapping = search_operator_mapping_api.get_by_id(pk=pk)

            # Build serializer
            search_operator_mapping_serializer = SearchOperatorMappingSerializer(
                instance=search_operator_mapping,
                data=request.data,
                partial=True,
            )

            # Validate and save search operator
            search_operator_mapping_serializer.is_valid(True)
            search_operator_mapping_serializer.save()

            return Response(
                search_operator_mapping_serializer.data, status=status.HTTP_200_OK
            )
        except ValidationError as validation_exception:
            content = {"message": validation_exception.detail}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.DoesNotExist:
            content = {"message": "Search operator not found."}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        """Delete a search operator mapping

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
            search_operator = search_operator_mapping_api.get_by_id(pk=pk)

            # delete object
            search_operator_mapping_api.delete(search_operator)

            # Return response
            return Response(status=status.HTTP_204_NO_CONTENT)
        except exceptions.DoesNotExist:
            content = {"message": "Workspace not found."}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        except Exception as api_exception:
            content = {"message": str(api_exception)}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
