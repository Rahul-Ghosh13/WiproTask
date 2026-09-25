Feature: User management API
  As an API automation engineer
  I want to manage users through the REST API
  So that user lifecycle behavior is verified end to end

  @smoke @authentication
  Scenario: Verify login with valid credentials
    Given a registered API user
    When I verify login with the registered credentials
    Then the response status should be 200
    And the API response message should be "User exists!"
    And the client should be authenticated

  @user-management
  Scenario: Create and retrieve a user
    Given a new API user payload
    When I create the API user
    Then the response status should be 201
    And the API response message should be "User created!"
    When I retrieve the user by email
    Then the response status should be 200
    And the returned user email should match the request email

  @user-management
  Scenario: Update and delete a user
    Given a registered API user
    When I update the API user name to "Updated API User"
    Then the response status should be 200
    And the API response message should be "User updated!"
    When I delete the API user
    Then the response status should be 200
    And the API response message should be "Account deleted!"
