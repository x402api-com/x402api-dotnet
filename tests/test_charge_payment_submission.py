import pathlib
import unittest


class ChargePaymentSubmissionTests(unittest.TestCase):
    def test_generated_method_sends_signature_header_and_no_body(self):
        source = pathlib.Path(
            "src/X402Api/Api/ProgrammaticChargesApi.cs"
        ).read_text()
        start = source.index(
            "public async Task<IChargesSubmitPaymentApiResponse> "
            "ChargesSubmitPaymentAsync"
        )
        end = source.index(
            "OnErrorChargesSubmitPaymentDefaultImplementation", start
        )
        method = source[start:end]

        self.assertIn('"/v1/charges/{charge_id}/payments"', method)
        self.assertIn('Headers.Add("PAYMENT-SIGNATURE"', method)
        self.assertIn("httpRequestMessageLocalVar.Method = HttpMethod.Post", method)
        self.assertNotIn("httpRequestMessageLocalVar.Content =", method)


if __name__ == "__main__":
    unittest.main()
