import sqlite3
import csv
import os
from django.db.models import Q
from rest_framework import generics, mixins
from postings.models import ApiPost
from .permissions import IsOwnerOrReadOnly
from .serializers import ApiPostSerializer
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from django.http import HttpResponse


class ApiPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'
    serializer_class = ApiPostSerializer

    def get_queryset(self):
        qs = ApiPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        latestId = ApiPost.objects.latest('id').id
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        cursor.execute("SELECT TrORTst FROM postings_apipost WHERE  id =" + str(latestId))
        x = [int(record[0]) for record in cursor.fetchall()]
        if x[0] == 0:
            def ConvertToCsvTest():
                cursor.execute("SELECT Length, AbsoluteLength, AvgSpeed, StartPressure, EndPressure,  AvgPressure, StartSize, EndSize, AvgSize, StartX, EndX, StartY, EndY, Area, Direction, MoveType, UserID FROM postings_apipost WHERE TrORTst = 0 ")
                results = cursor.fetchall()
                with open("train.csv", "w", newline='') as csv_file:              # Python 3 version
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(results)
                cursor.close()
            ConvertToCsvTest()
        else:
            def ConvertToCsvTest():
                cursor.execute("SELECT Length, AbsoluteLength, AvgSpeed, StartPressure, EndPressure,  AvgPressure, StartSize, EndSize, AvgSize, StartX, EndX, StartY, EndY, Area, Direction, MoveType, UserID FROM postings_apipost WHERE TrORTst =" + str(latestId))
                results = cursor.fetchall()
                with open("Test.csv", "w", newline='') as csv_file:              # Python 3 version
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(results)
                cursor.close()
            ConvertToCsvTest()
        # print("current id =  \n", latestId)

        HEADERS = list(pd.read_csv("d:/csv files/fullsheet train1.csv").head(0))
        clf = RandomForestClassifier()

        def training_model():
            OUTPUT_PATH1 = "d:/csv files/fullsheet train1.csv"
            traindata = pd.read_csv(OUTPUT_PATH1)
            train_x, train_y = traindata[HEADERS[1:-1]], traindata[HEADERS[-1]]
            trained_model = clf.fit(train_x, train_y)
            # print ("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
            return trained_model

        def testing_model(trained_model):
            OUTPUT_PATH2 = "d:/csv files/fullsheet test1.csv"
            testdata = pd.read_csv(OUTPUT_PATH2)
            test_x, test_y = testdata[HEADERS[1:-1]], testdata[HEADERS[-1]]
            predictions = trained_model.predict(test_x)
            print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
            abc = confusion_matrix(test_y, predictions)
            print("Confusion Matrix \n", abc)
            confidence = clf.score(test_x, test_y)
            print("confidence \n", confidence)

        def main():
            np.random.seed(0)
            t = training_model()
            testing_model(t)

        main()
        return HttpResponse("result = 125")

    def post(self, request, *args, **kwargs):
        # return self.render_json_response(
         #   {"message": "your data has been saved"})
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ApiPostRudView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = ApiPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ApiPost.objects.all()

    def get_queryset(self):
        return ApiPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


latestId = ApiPost.objects.latest('id').id
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT TrORTst FROM postings_apipost WHERE  id =" + str(latestId))
# print("trainOrTest Value = ", cursor.fetchone())
x = [int(record[0]) for record in cursor.fetchall()]
print("trainOrTest Value = ", x[0])
