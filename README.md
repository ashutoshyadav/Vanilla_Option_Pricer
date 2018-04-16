# Vanilla Option Pricer
----
> _This is a simple Restful API implementation for calculating the Price and other greeks using Black-Scholes Formula for Vanilla Options.The API offers GET, PUT and POST methods where the GET method is used to render the HTML template for the UI._

- ## URL
>        `/vop/`

- ## Method
    - ### **`GET`**
        - URL 
          > `/vop/`
        - URL Params
             > `None`
        - Data Params
             > `None`
        - Sucess
            - Code : `200`
            - Response: `HTML Template for the Home Page'
             ![alt-text](https://github.com/ashutoshyadav/Vanilla_Option_Pricer/blob/master/template.JPG "Home Page Template")
        - Error Response
            - Code : `404`
            - Response: `Page Not Found`
        - Sample Call
            > `'http://127.0.0.1:5000/vop/`
    - ### **`POST`**
        - URL
          > `/vop/`
        - URL Params
            > `None`
        - Data Params
             - Spot Price `(name = spot)`
             - Strike Price `(name= strike)`
             - Volatility `(name = vol)`
             - Rate `(name = rate)`
             - Maturity Date `(name= maturity)`
             - Strike Date `(name = strike-date)`
         - Success
              - Code : `200`
              - Response : <br/>
              ```javascript
                          { 
                              "type" :         "call"
                              "Spot":          100,
                              "Strike":        110,
                              "Rate":          0.02,
                              "Vol":           0.4,
                              "StrikeDate":    "23-Feb-18",
                              "MaturityDate":  "23-Feb-19",
                              "Price" :        22.89969,
                              "Delta" :        0.72082,
                              "Gamma" :        0.00842,
                              "Theta" :       -15.86969,
                              "Vega" :         0.33569
                          }
          - Sample Call
              ```javascript
                    var data = {
                      spot : 100,
                      strike: 100,
                      vol: 0.4,
                      rate : 0.02,
                      type : "call",
                      maturity : "22-03-2018",
                      'strike-date': "22-03-2017"
                    };
                    $.ajax({
                      type : 'post',
                      url : '/vop/',
                      dataType:'json',
                      data : data,
                      success: function(result){
                        $('#result').html(text.price);
                      }
                    });
     - ### **`PUT`**
          - URL
              > `/vop/`
          - URL params
              > `None`
          - Data params
              ```javascript
              {
                "Products": [
                  {
                    "ProductName": "Put",
                    "ProductParams":
                    {
                      "Underlying": "UnderlyingB",
                      "Spot": 100,
                      "Strike": 100,
                      "Rate": 0,
                      "Vol": 0.25,
                      "StrikeDate": "23-Feb-18",
                      "MaturityDate": "23-Feb-19"
                    }
                  }
                 ]
               }
           - Success
                - Code : `200`
                - Response : 
                ```javascipt
                      {
                        "Products": [
                          {
                            "ProductName": "Put",
                            "ProductParams":
                            {
                              "Underlying": "UnderlyingB",
                              "Spot": 100,
                              "Strike": 110,
                              "Rate": 0.02,
                              "Vol": 0.4,
                              "StrikeDate": "23-Feb-18",
                              "MaturityDate": "23-Feb-19"
                            },
                            "Price" :        22.89969,
                            "Delta" :        0.72082,
                            "Gamma" :        0.00842,
                            "Theta" :       -15.86969,
                            "Vega" :         0.33569
                          }
                        ]
                      }
            - Sample Call
              ```python 
                data =	{
                    "Products": [
                      {
                        "ProductName": "Call",
                        "ProductParams":
                        {
                          "Underlying": "UnderlyingA",
                          "Spot": 1,
                          "Strike": 1,
                          "Rate": 0,
                          "Vol": 0.25,
                          "StrikeDate": "23-Feb-18",
                          "MaturityDate": "22-Feb-19"
                        }
                      },
                      {
                        "ProductName": "Put",
                        "ProductParams":
                        {
                          "Underlying": "UnderlyingA",
                          "Spot": 100,
                          "Strike": 100,
                          "Rate": 0.02,
                          "Vol": 0.4,
                          "StrikeDate": "23-Feb-18",
                          "MaturityDate": "22-Feb-19"
                        }
                      }
                    ]
                  }
                  data = json.dumps(data)
                  headers = {"Content-Type": "application/json", 'data':data}
                  response = requests.put(url, data=data, headers=headers)
                  print(response.text)

                  
          
