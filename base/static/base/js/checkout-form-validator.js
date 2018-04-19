// Wait for the DOM to be ready
$(function() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"

  $('#order-form').validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      name: "required",
      address: "required",
      email: {
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true
      },
      number: {
        required: true,
        digits: true,
        number: true
      },
      count: {
        required : true,
        min : 1,
        max : 100
      },
      comment: {
        required: false
      }
    },
    // Specify validation error messages
    messages: {
      name: "Введіть ваше ім'я",
      address: "Введіть вашу адресу",
      number: {
        required: "Введіть номер телефону",
        digits : "Введіть лише цифри",
        number : "Введіть лише цифри"
      },
      email: "Введіть правильну email адресу",
      count: {
        required: "Введіть правильну кількість осіб",
        min: "Мінімальна кількість осіб - 1",
        max: "Надто багато"
      }
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      // form.submit();
    }
  });
});