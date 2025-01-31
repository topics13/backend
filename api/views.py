from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.http import HttpResponse

class crop_predict(APIView):
    SAMPLE_CROP_ATTRIBUTES = [
            90,
            40,
            40,
            20,
            80,
            7,
            200
        ]

    def get(self, request):
        return Response({
            'msg': 'success',
            'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
        })
    
    def post(self, request):
        from controllers.crop_predict import crop_predict

        if not request.data.get('crop_attributes'):
            return Response({
                'msg': 'No crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        crop_attributes = request.data.get('crop_attributes')

        if len(crop_attributes) != len(self.SAMPLE_CROP_ATTRIBUTES):
            return Response({
                'msg': 'Wrong number of crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            return Response({
                'msg': 'success',
                'crop_attributes': crop_attributes,
                'prediction': crop_predict(crop_attributes)[0]
            })
        except:
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class fertilizer_predict(APIView):
    SAMPLE_CROP_ATTRIBUTES = {
        'cropname': 'Rice',
        'nitrogen': 50,
        'phosphorus': 50,
        'pottasium': 50
    }

    def get(self, request):
        return Response({
            'msg': 'success',
            'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
        })
    
    def post(self, request):
        from controllers.fertilizer_predict import fertilizer_predict

        if not request.data.get('crop_attributes'):
            return Response({
                'msg': 'No crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        crop_attributes = request.data.get('crop_attributes')

        if len(crop_attributes) != len(self.SAMPLE_CROP_ATTRIBUTES):
            return Response({
                'msg': 'Wrong number of crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            return Response({
                'msg': 'success',
                'crop_attributes': crop_attributes,
                'prediction': fertilizer_predict(crop_attributes)
            })
        except:
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class disease_predict(APIView):
    
    def post(self, request):

        if not request.data.get('crop_image'):
            return Response({
                'msg': 'Crop Image not provided'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        crop_image = request.data.get('crop_image').read()

        from controllers.disease_predict import disease_predict

        prediction = disease_predict(crop_image)
        
        return Response({
            'msg': 'success',
            'prediction': prediction
        })
        
        try:
            return Response({
                'msg': 'success',
                'prediction': disease_predict(crop_image)
            })
        except Exception as e:
            print(e)
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class market_stats(APIView):
    SAMPLE_CROP_ATTRIBUTES = {
        'state': 'Punjab',
        'crop': 'Rice'
    }

    def get(self, request):
        return Response({
            'msg': 'success',
            'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
        })
    
    def post(self, request):
        from controllers.market_stats import market_stats

        if not request.data.get('crop_attributes'):
            return Response({
                'msg': 'No crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        crop_attributes = request.data.get('crop_attributes')

        return Response({
                'msg': 'success',
                'crop_attributes': crop_attributes,
                'prediction': market_stats(crop_attributes)
            })

        try:
            return Response({
                'msg': 'success',
                'crop_attributes': crop_attributes,
                'prediction': market_stats(crop_attributes)
            })
        except:
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)