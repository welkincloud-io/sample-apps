
## Welkin's V8 API Usage in python


This is examples of using python code to connect to Welkin's v8 APIs.

You can access Welkin V8 API documentation.
[Welkin V8 Documentation](https://developers.welkinhealth.com/ "Welkin V8 Documentation")

---
### Initial Setup


#### Creating API Client
1. Create API client in your Organization
Navigate to Admin -> API Clients -> Create Client
Copy the Client Name and Secret Key or download it.
Navigate to the API Client page you created

2. Configure appropriate access for the client (Instance Access, Roles, Security Policies)
Reminder: Security Policies and Roles are defined in the Designer and assigned in the Admin

For this example we will assume Client Name is **VBOPNRYRWJIP** and Secret Key is **+}B{KGTG6#zG%P;tQm0C**

---
### Configuration

The draft_config.json file should be used in  designer 'create draft' configuration
1. Go to Change Summary - Create Draft

![designer](docs/static/designer1.jpg)
   
2. Choose from file and browse.

![create_draft](docs/static/create_draft.jpg)
   
3. Choose draft_config.json file from root path of Sample app.

![draft_config](docs/static/draft_config.jpg)
   
Once you finished the steps, there are several variables in URL structure we need to setup before using this Repo.

`
**Note: Set API client name, tenant name,
instance name, secret and environment(stg/live) in config.py file** 

1. First variable is your Tenant (orgnization) name.
   
2.  Second variable is your client name. 
In order to Authenticate in Welkin, client name, secret required.

3.  Third variable  is Instance (Environment) - This is a separate database inside a tenant. 
    Typical customer will have 2-3 instances, representing customer development, 
    testing and live environments, as you build out your Welkin care program.
    
4.  Forth variable is Secret.
5.  Fifth varible is ENV which will represent testing or live environments. 
    It's Value will be **stg** or **live**. 
    
---

### Using this Repo
1. set values in config.py file
2. Generate token by running /utils/generate_token.py file.
3. Run Scripts by following instruction provided in docstring. There is Json file with
same name associated with script, edit json file before running script.
   
---
### Troubleshooting steps 

#### 400 Bad Request
A 400 status code means that the server could not process an API request due to invalid syntax. 
A few possibilities why this might happen are:
- A typo or mistake while setting  config.py variables, such as mistyping the API client name, tenant name,
    instance name, secret and environment(stg/live), check the URL while running script if any 
  variable showing None value.
  
- A malformed JSON body, for example, missing a set of double-quotes, or a comma. 
  If you need to make an API request with a JSON body.
  
- The request is missing authentication information, or the Authorization header provided could not be validated
make sure to run util/generate_token.py before running  any script in this repo. 
  
#### 401 Unauthorized

The 401 Unauthorized status code is returned when the API request is missing authentication credentials or 
the credentials provided are invalid.

#### 403 Forbidden
The 403 Forbidden status code looks similar to the 401 code, but they shouldn't be confused with each other.

Usually, when you see the 403 status code, the API request that is being made includes some form of authorization. But, different from the 401 status code, the server does recognize the authorization credentials and accepts is as valid. The issue this time is that the authenticated user cannot access the resource for that endpoint. For example, the user might be trying to access account-level information that's only viewable by the account administrator, and the credentials being passed on the API request are for a regular user account.

Another reason this status code might be returned is in case the user did not request an API access token with the correct permissions.

To fix the API call for those two situations, make sure that the credentials you are using have the access-level required by the endpoint, or that the access token has the correct permissions.

A less common reason we might see this error is if we're not explicit about the Accept header value. Some APIs require you to include those headers on requests. That way, the server knows what information the client is sending, and also what format they expect to receive in return.

#### 404 Not Found
404 Not Found one of those status codes that we don't have to be working with APIs to see. But, specifically for APIs, it can usually mean a few different things:

- The endpoint does not exist

- The endpoint exists, but the resource cannot be found

- The endpoint exists and the resource can be found, but the user does not have the required permissions to access it, and so the server returns a 404 status code

For the first two cases, there's not much we can do as an API user, except double-check that the endpoint really does exist in the documentation, or double-check that there are no misspellings or typos.

For the third case, the advice is similar to what we covered in the previous status code, 403. Make sure that the authorization credentials you are using actually have access to that endpoint, as some APIs might return a 404 error instead of 403.