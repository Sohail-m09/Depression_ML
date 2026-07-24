from pydantic import BaseModel


class DepressionInput(BaseModel):
    age: int
    gender: str
    marital_status: str
    education_level: str
    employment_status: str
    sleep_hours: int
    physical_activity_hours_per_week: int
    screen_time_hours_per_day: int
    social_support_score: int
    work_stress_level: int
    academic_pressure_level: int
    job_satisfaction_score: int
    financial_stress_level: int
    working_hours_per_week: int
    anxiety_score: int
    depression_score: int
    stress_level: int
    mood_swings_frequency: int
    concentration_difficulty_level: int
    panic_attack_history: int
    family_history_mental_illness: int
    previous_mental_health_diagnosis: int
    therapy_history: int
    substance_use: int