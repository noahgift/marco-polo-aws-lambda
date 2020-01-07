def lambda_handler(event, context):
      if 'body' in event:
        event = json.loads(event["body"])
        if event["name"] == "Marco":
          return "Polo"
      return None
