from rest_framework import generics
from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer