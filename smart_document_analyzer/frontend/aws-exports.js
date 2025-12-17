const awsmobile = {
    aws_project_region: "ap-south-1",
    aws_cognito_region: "ap-south-1",
    aws_user_pools_id: "",
    aws_user_pools_web_client_id: "",
    aws_appsync_graphqlEndpoint: "",
    aws_appsync_region: "ap-south-1",
    aws_appsync_authenticationType: "",
    aws_cloud_logic_custom: [
        {
            name: "SmartDocAPI",
            endpoint: "https://your-api-id.execute-api.ap-south-1.amazonaws.com/prod",
            region: "ap-south-1"
        }
    ]
};

export default awsmobile;
