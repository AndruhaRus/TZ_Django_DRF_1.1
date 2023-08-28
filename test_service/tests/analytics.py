from tests.models import Question, TestResult

class TestAnalytics:
    @staticmethod
    def get_test_pass_count():
        return TestResult.objects.count()

    @staticmethod
    def get_success_rate():
        total_results = TestResult.objects.count()
        successful_results = TestResult.objects.filter(score__gte=50).count()
        success_rate = (successful_results / total_results) * 100
        return success_rate

    @staticmethod
    def get_most_difficult_question():
        difficult_question = Question.objects.order_by('is_correct').first()
        return difficult_question