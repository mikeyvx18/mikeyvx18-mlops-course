# Week 03 Lab

Build an ingestion pipeline from a public API/dataset; handle errors and retries.

Starter files for this week's lab will be added here before the lab session
(pulled into your repo via `git fetch upstream && git merge upstream/main`,
as introduced in the Week 1 lab).

## Reflection

### 1. Which failure type was easiest/hardest to test and why?

The timeout failure was straightforward to test by temporarily setting the request timeout to a very small value. The connection error was also easy to test by using an invalid API hostname. The HTTP error was tested by providing an invalid latitude value. The timeout test was useful because it demonstrated the retry behavior and exponential backoff clearly.

### 2. How did exponential backoff change timing? Did you observe the printed delays?

Exponential backoff increased the waiting time between retry attempts. During the timeout test, the program printed delays of 1 second, 2 seconds, and 4 seconds before the next attempts. This demonstrated that the delay increased after each failed attempt instead of retrying immediately.

### 3. Why do we retry timeouts/connections but not HTTP 400?

Timeouts and connection errors can be temporary problems, so retrying the request may allow a later attempt to succeed. An HTTP 400 error indicates that the API rejected the request because the request itself was invalid. Retrying the same invalid request would not normally fix the problem, so the pipeline does not retry HTTP 400 errors.

### 4. What data contract would you specify for consumers?

I would specify a data contract that defines the expected schema, field names, data types, units, and meanings of each weather field. For example, temperature should be clearly identified as degrees Celsius, wind speed as kilometers per hour, and relative humidity as a percentage. The contract should also define expected availability and freshness requirements (SLA), how missing or invalid data should be handled, and how API/schema changes will be communicated and managed.