from openfisca_us.model_api import *


class is_young_adult_for_medicaid(Variable):
    value_type = bool
    entity = Person
    label = "Young adults"
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/42/1396d#a_i"

    def formula(person, period, parameters):
        age = person("age", period)
        ma = parameters(period).hhs.medicaid.eligibility.categories.young_adult
        is_young_adult = ma.age_range.calc(age)
        income = person("medicaid_income_level", period)
        state = person.household("state_code_str", period)
        income_limit = ma.income_limit[state]
        return is_young_adult & (income < income_limit)
