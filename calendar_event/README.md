## Calendar Events
The Calendar Event API provides different flavors of event resources, more information can be found in
[Calendar Events Documentaion](https://developers.welkinhealth.com/#create-calendar-event).



It is a typical calendar API to create and manage events

URL Structure: {{url}}/{{tenantName}}/{{instanceName}}/calendar/events

in our example it would be:

https://api.live.welkincloud.io/gh/sb-demo/calendar/events

#### Fields description:

|Field Name |	Supported Values
|---|---|
eventType  |	"GROUP_THERAPY", "APPOINTMENT", "LEAVE", "ENCOUNTER"
eventStatus	|  "SCHEDULED", "CANCELLED", "COMPLETED", "MISSED"
eventMode	| "IN-PERSON", "CALL", "VIDEO"
participantRole |	"patient", "psm"

| Field Name |	Field description
|---|---|
hostId	| ID of user which owns the event
additionalInfo |	Custom object without strict defined structure
externalId	| Custom string for object identification, must be different for each event
externalIdUpdatedAt |	Timestamp when calendar event externalId has been updated

Please note that participants field must contain participant with id=hostId

---
### Encounters
APIs for working with an encounter 
infrastructure: records, assessment links, comments, template, disposition, disposition-formation.

HTTP Request
POST /{tenantName}/{instanceName}/patients/{patientId}/encounters

in our example it would be:

POST https://api.live.welkincloud.io/gh/sb-demo/patients/620ef7f0-2ba9-48e1-8e0f-a47f40890bf4/encounters


How to create encounter template in designer?
To create encounter template we need to create "Forms" in the visual  component.
---

## Encounter creation:

### 1. Legacy:
1. Create calendar event (POST /events)

**POST** https://api.live.welkincloud.io/{{tenantName}}/{{instanceName}}/calendar/events

{
	"eventType": "ENCOUNTER",
	...
}

2. Create encounter with calendar event id reference (POST /encounters)

**POST** https://api.live.welkincloud.io/{{tenantName}}/{{instanceName}}/patients/{{patientID}}/encounters

{	"title": "sample-title",
	"templateName": "enc-template",
	"calendarEventId": "e52e476e-7fe9-44ba-b5ad-43296760dc2a"
}

**Restrictions:**

- Calendar event must by type of ENCOUNTER
- Cal event shouldn’t be assigned to any encounter
- Cal event must be in the future

**Execution  steps:**

NOTE: There is a Json file with the same name associated with each script. To customize the data to be loaded, 
edit the json file before running the script.
1. generate token using utils/generate_token.py
2. RUN  create_calendar_event.py to create calendar event. copy Calendar event Id from successful response.
3. RUN  create_encounter_for_patient.py 

Step 3 will create encounter for patient. We can assign new event in 
addition to  created encounter by step 4:

4. Assign new event: 
PATCH /encounters/{{encounterId}}
   
**PATCH**  https://api.live.welkincloud.io/{{tenantName}}/{{instanceName}}/patients/{patientId}/encounters/{encounter_id}
   

{
	"calendarEventId": "e52e476e-7fe9-44ba-b5ad-43296760dc2a"
}



---

###  2. New workflows:


Encounter creation: 

Create encounter: POST /encounters

**POST** https://api.live.welkincloud.io/{{tenantName}}/{{instanceName}}/patients/{{patientID}}/encounters

```
{
	"templateName": "enc-template",
 		…,
	"calendarEvent": {
    	"eventTitle": "Title",
    	"eventType": "ENCOUNTER", 
    	“startDateTime:”: “...”,
            “endDateTime:”: “...”,
			...
	}
}
```

Full event DTO directly passed in the “calendarEvent” field, encounter service will internally call calendar service with this dto and create the event for encounter. 

Calendar API will disable direct creation of events with ‘ENCOUNTER’ type. So this API call will fail:
POST /events
{
	…,
	“eventType”: “ENCOUNTER”
}


---



