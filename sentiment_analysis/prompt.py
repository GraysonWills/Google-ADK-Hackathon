ROOT_AGENT_PROMPT = """
Your task is to give back the following pieces of information from the session:

<therapist_profile>
{therapist_profile}
</therapist_profile>
<session_data>{session_data}</session_data>
<patient_id>{patient_id}</patient_id>
<session_type>{session_type}</session_type>
<session_date>{session_date}</session_date>
<session_start_time>{session_start_time}</session_start_time>
<session_duration>{session_duration}</session_duration>
<audio_analysis_results>{audio_analysis_results}</audio_analysis_results>
<video_analysis_results>{video_analysis_results}</video_analysis_results>
<combined_sentiment_score>{combined_sentiment_score}</combined_sentiment_score>
<emotional_state_assessment>{emotional_state_assessment}</emotional_state_assessment>
<behavioral_patterns>{behavioral_patterns}</behavioral_patterns>
<treatment_progress>{treatment_progress}</treatment_progress>
<next_session_recommendations>{next_session_recommendations}</next_session_recommendations>
<session_notes>{session_notes}</session_notes>
<follow_up_actions>{follow_up_actions}</follow_up_actions>
<risk_assessment_status>{risk_assessment_status}</risk_assessment_status>
<initialized>{initialized}</initialized>
"""