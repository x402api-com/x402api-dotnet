import pathlib
import unittest


class PaymentReceiptStatusTests(unittest.TestCase):
    def setUp(self):
        self.source = pathlib.Path(
            "src/X402Api/Api/OrdersAndPaymentsApi.cs"
        ).read_text(encoding="utf-8")

    def test_receipt_response_exposes_distinct_200_and_202_models(self):
        interface_start = self.source.index(
            "public interface IPaymentsRetrieveReceiptApiResponse"
        )
        interface_end = self.source.index("\n    /// <summary>", interface_start)
        response_interface = self.source[interface_start:interface_end]

        self.assertIn("IOk<X402Api.Model.PaymentReceipt?>", response_interface)
        self.assertIn(
            "IAccepted<X402Api.Model.PaymentReceiptStatus?>", response_interface
        )
        self.assertIn("bool IsOk { get; }", response_interface)
        self.assertIn("bool IsAccepted { get; }", response_interface)

    def test_accepted_response_deserializes_payment_status_not_receipt(self):
        class_start = self.source.index(
            "public partial class PaymentsRetrieveReceiptApiResponse"
        )
        class_end = self.source.index(
            "private void AfterReceiptVerificationKeysRetrieveDefaultImplementation",
            class_start,
        )
        response_class = self.source[class_start:class_end]

        self.assertIn("public bool IsOk => 200 == (int)StatusCode;", response_class)
        self.assertIn(
            "public bool IsAccepted => 202 == (int)StatusCode;", response_class
        )
        self.assertIn(
            "public X402Api.Model.PaymentReceiptStatus? Accepted()", response_class
        )
        self.assertIn(
            "JsonSerializer.Deserialize<X402Api.Model.PaymentReceiptStatus>",
            response_class,
        )
        self.assertIn(
            "public bool IsDefault => !IsOk && !IsAccepted",
            response_class,
        )


if __name__ == "__main__":
    unittest.main()
