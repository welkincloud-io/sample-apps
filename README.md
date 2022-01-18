
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
