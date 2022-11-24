import boto3


def scan_database(table, scan_kwargs=None):
    if scan_kwargs is None:
        scan_kwargs = {}
    # aws_access_key_id = Takes the access key_id
    # aws_secret_access_key = key
    # region_name = Name of the region
    dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIAVLFFKFZSR2PIHS2L',
                              aws_secret_access_key='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', region_name='us-east-1')
    table = dynamodb.Table(table)

    complete = False
    records = []
    while not complete:
        try:
            response = table.scan(**scan_kwargs)
        except Exception as error:
            raise Exception('Error quering DB: {}'.format(error))

        records.extend(response.get('Items', []))
        next_key = response.get('LastEvaluatedKey')
        scan_kwargs['ExclusiveStartKey'] = next_key

        complete = True if next_key is None else False
    return records
