package uc.seng301.petbattler.lab5.cucumber;


import io.cucumber.junit.platform.engine.Constants;
import org.junit.platform.suite.api.ConfigurationParameter;
import org.junit.platform.suite.api.IncludeEngines;
import org.junit.platform.suite.api.Suite;
import org.junit.platform.suite.api.SelectClasspathResource;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("uc/seng301/petbattler/lab5/cucumber")
@ConfigurationParameter(key = Constants.GLUE_PROPERTY_NAME,value = "uc/seng301/petbattler/lab5/cucumber/step_definitions")
@ConfigurationParameter(key = Constants.PLUGIN_PROPERTY_NAME,value = "pretty, html:target/cucumber-report/cucumber.html")
public class RunCucumberTest {
}
