Feature: TC_search0

    Scenario: Find a fly succesfuly
        Given I go to the site "space_and_beyond"
        #When I select a valid departing date
        #When I select a valid returning date
        When I select valid quantity adults
        When I click on select destination
        Then I should be on "destination"
        Then I should find planets cards