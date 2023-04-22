# Generated by Django 4.0.8 on 2023-04-19 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('z_tab_pmb_quantum', '0001_initial'),
        ('g_measures', '0001_initial'),
        ('a_hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_category_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Category Code')),
                ('risk_category_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Category Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Category',
                'db_table': 'risk_category',
                'ordering': ['risk_category_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskMitigationStrategyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_mitigation_strategy_type_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Mitigation Strategy Type Code')),
                ('risk_mitigation_strategy_type_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Mitigation Strategy Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Mitigation Strategy Type',
                'db_table': 'risk_mitigation_strategy_type',
                'ordering': ['risk_mitigation_strategy_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskMonitoringMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_monitoring_metric_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Monitoring Metric Code')),
                ('risk_monitoring_metric_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Monitoring Metric Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Monitoring Metric',
                'db_table': 'risk_monitoring_metric',
                'ordering': ['risk_monitoring_metric_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskProbability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_probability_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Probability Code')),
                ('risk_probability_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Probability Title')),
                ('risk_probability_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Risk Probability Value')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Probability',
                'db_table': 'risk_probability',
                'ordering': ['risk_probability_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskSeverity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_severity_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Severity Code')),
                ('risk_severity_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Severity Title')),
                ('risk_severity_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Risk Severity Value')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Severity',
                'db_table': 'risk_severity',
                'ordering': ['risk_severity_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskTimeFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_timeframe_code', models.CharField(max_length=5, unique=True, verbose_name='Risk TimeFrame Code')),
                ('risk_timeframe_title', models.CharField(max_length=55, unique=True, verbose_name='Risk TimeFrame Title')),
                ('risk_timeframe_value', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Risk TimeFrame Value')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk TimeFrame',
                'db_table': 'risk_timeframe',
                'ordering': ['risk_timeframe_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskUnderlyingAssumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_underlying_assumption_code', models.CharField(max_length=5, unique=True, verbose_name='Risk Underlying Assumption Code')),
                ('risk_underlying_assumption_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Underlying Assumption Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Risk Underlying Assumption',
                'db_table': 'risk_underlying_assumption',
                'ordering': ['risk_underlying_assumption_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Risks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('cost_or_schedule', models.CharField(default='Cost', max_length=8, verbose_name='cost or Schedule')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.company', verbose_name='Company ID')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.personnel', verbose_name='Personnel ID')),
                ('pmb_L03_wp', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='z_tab_pmb_quantum.pmbl03wp', verbose_name='PMB L03 WP ID')),
                ('risk_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskcategory', verbose_name='Risk Category ID')),
                ('risk_monitoring_metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskmonitoringmetric', verbose_name='Risk Monitoring Metric ID')),
                ('risk_probability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskprobability', verbose_name='Risk Probability ID')),
                ('risk_severity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskseverity', verbose_name='Risk Severity ID')),
                ('risk_timeframe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.risktimeframe', verbose_name='Risk TimeFrame ID')),
                ('risk_underlying_assumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskunderlyingassumption', verbose_name='Risk Underlying Assumption ID')),
                ('stakeholder_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.stakeholderroles', verbose_name='Stakeholder Role ID')),
            ],
            options={
                'verbose_name_plural': 'Risks',
                'db_table': 'risk',
                'ordering': ['risk_category'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskMitigationStrategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rms_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Mitigation Strategy Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('rms_implementation_date', models.DateTimeField(blank=True, null=True, verbose_name='Risk Mitigation Strategy Implementation Date')),
                ('rms_implementation_estimated_costs', models.DecimalField(blank=True, decimal_places=2, help_text='Estimated cost of the risk mitigation strategy implementation', max_digits=18, null=True, verbose_name='Risk Mitigation Strategy Implementation Estimated Costs')),
                ('rms_implementation_actual_costs', models.DecimalField(blank=True, decimal_places=2, help_text='Actual cost of the risk mitigation strategy implementation', max_digits=18, null=True, verbose_name='Risk Mitigation Strategy Implementation Actual Costs')),
                ('rms_success_metric', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Risk Mitigation Strategy Success Metric')),
                ('rms_success_check_date', models.DateTimeField(blank=True, null=True, verbose_name='Risk Mitigation Strategy Success Check Date')),
                ('rms_success_failure_comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Risk Mitigation Strategy Success or Failure Comments')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.risks', verbose_name='Risk ID')),
                ('rms_success_check', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_measures.boolean', verbose_name='Risk Mitigation Strategy Success Check')),
                ('rms_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskmitigationstrategytype', verbose_name='Risk Mitigation Strategy Type ID')),
            ],
            options={
                'verbose_name_plural': 'Risk Mitigation Strategies',
                'db_table': 'risk_mitigation_strategy',
                'ordering': ['rms_title'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RiskContingencyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rcp_title', models.CharField(max_length=55, unique=True, verbose_name='Risk Contingency Plan')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('trigger', models.CharField(blank=True, help_text='Description of the condition which will trigger the execution of the risk contingency plan', max_length=2000, null=True, verbose_name='Trigger')),
                ('rcp_implementation_date', models.DateTimeField(blank=True, null=True, verbose_name='Risk Contingency Plan Implementation Date')),
                ('rcp_implementation_estimated_costs', models.DecimalField(blank=True, decimal_places=2, help_text='Estimated cost of the Risk Contingency Plan implementation', max_digits=18, null=True, verbose_name='Risk Contingency Plan Implementation Estimated Costs')),
                ('rcp_implementation_actual_costs', models.DecimalField(blank=True, decimal_places=2, help_text='Actual cost of the Risk Contingency Plan implementation', max_digits=18, null=True, verbose_name='Risk Contingency Plan Implementation Actual Costs')),
                ('rcp_success_check_date', models.DateTimeField(blank=True, null=True, verbose_name='Risk Contingency Plan Success Check Date')),
                ('rcp_success_failure_comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Risk Contingency Plan Success or Failure Comments')),
                ('rcp_success_check', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_measures.boolean', verbose_name='Risk Contingency Plan Success Check')),
                ('risk_mitigation_strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='r_risk.riskmitigationstrategies', verbose_name='Risk Mitigation Strategy ID')),
            ],
            options={
                'verbose_name_plural': 'Risk Contingency Plan',
                'db_table': 'risk_contingency_plan',
                'ordering': ['rcp_title'],
                'managed': True,
            },
        ),
    ]
