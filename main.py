import phonenumbers
import requests
from phonenumbers import carrier, geocoder, timezone

#-----------------------------------------------------------------------------------------------------------------------

print("""
    @@@@@@@@@   @        @  @     @  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@
    @       @   @ @      @  @    @         @               @
    @       @   @  @     @  @   @          @               @
    @       @   @   @    @  @  @           @               @
    @@@@@@@@@   @    @   @  @@@            @               @
    @       @   @     @  @  @  @           @               @
    @       @   @      @ @  @   @          @               @
    @       @   @       @@  @    @         @               @
    @       @   @        @  @     @  @@@@@@@@@@@@@         @

""")
print("Auther:- Ankit Shukla")
print("Contributer: Animo Tanixome")
print("Github:- github.com/ankit637")
#-----------------------------------------------------------------------------------------------------------------------



def get_phone_number_info(phone_number):
    phone_number = phonenumbers.parse(phone_number)
    if phonenumbers.is_valid_number(phone_number):
        print('Phone Number: {}'.format(phone_number.national_number))
        print('Region: {}'.format(timezone.time_zones_for_number(phone_number)[0]))
        print('Service Provider: {}'.format(carrier.name_for_number(phone_number, "en")))
        print('Country: {}'.format(geocoder.description_for_number(phone_number, "en")))
        print('Number Type: {}'.format('Mobile' if phonenumbers.is_possible_number(phone_number) else 'Fixed line'))

        # Using NumVerify API to get additional information
        access_key = '808234ca87efe9f02fff422f8ae89431'  # Get your API key from https://numverify.com/
        url = 'http://apilayer.net/api/validate'
        params = {'access_key': access_key, 'number': phone_number.national_number}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            print('Carrier: {}'.format(data['carrier']))
            print('Line Type: {}'.format(data['line_type']))
            print('Location: {}'.format(data['location']))
        else:
            print('Unable to fetch additional information.')
    else:
        print("Invalid phone number. Please enter a valid mobile number.")


if __name__ == '__main__':
    mobile_no = input("Enter Phone number with country code (+xx xxxxxxxxx): ")
    get_phone_number_info(mobile_no)
