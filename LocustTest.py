from locust import HttpUser, task
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU4MzM0MDUsImlhdCI6MTcxNTgzMTYwNSwidXNlcl90eXBlIjoiIiwicHJvZHVjdF9yb2xlcyI6W10sImF1dGhvcml0aWVzIjpbXSwiY29tcGFueV9pZHMiOiIiLCJwIjoiY2I5MDAyYjVhNjI1ZmY3OTgyNDA5YWJjLTg1NTdmNGM5YWRkNWFjNTIyZjY4N2JjMzVhMzFmYzk1Y2Q2YjllNWIiLCJlIjoiODgxNTdiNjA2ZDQ5NzUxYzAxMTIxODIyLWM5Zjk3ODE1OWYzYTI3ZjFlYzZmYzg0MTdmMDcwMjNiNjMzM2RmODdkOWQ4ZDVlYyJ9.RGISz4oKKQKvPwMetzTi4Y9ap98u5vwxoYYAPcnZlSg"
class HelloWorldUser(HttpUser):
        @task
        def fileType(self):
           self.client.post (
                        url=  "http://gym-master.apps.ocp-new-dev.bri.co.id/api/ukln-mass-transaction/mapping/file-type",
  
                       headers={"authorization": "Bearer "+ token},
                         json = {
                            "companyId": "12346013",
                              "fileType": ""
                               }
                  
                )
           

  #      @task
 #        def loginV2(self):
   #         self.client.post(
      #               url="/api/auth/v2/login",
   #                  headers={"x-signature": signature},
      #               json= {
      #                      "username": "CU_LKL_S",
      #                       "password": "Nsel@1234",
      #                       "branchCode": "LUKOIL"
       #                  }
       #          )
#locust -f LocustTest.py
#http://gym-master.apps.ocp-new-dev.bri.co.id
#Invoice Smart Billing Management 
#    self.client.post(
#                         url="http://gym-master.apps.ocp-new-dev.bri.co.id/api/create-briva-upload/billing-detail",
#                         headers={"authorization": "Bearer "+ token},
#                         json= {
#                             "body": {"billingDetailId": "70566"}
#                         }
#                 )
