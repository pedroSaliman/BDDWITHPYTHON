Feature:login success admin area nopcommerce
  Scenario:Login successfully
    Given the user can launsh the browser
     When the user open the page as "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
     Then the user enter email as "admin@yourstore.com" and password as "admin"
     Then the user click to login button
     Then the user verify login success
      And the user close the browser


