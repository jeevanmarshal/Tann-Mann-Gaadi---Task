import { useState } from 'react';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    email: ''
  });

  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    // Simulate API call for now (will be replaced with actual backend call)
    setTimeout(() => {
      console.log('Form Data Submitted:', formData);
      setIsSubmitting(false);
      setIsSubmitted(true);

      // Reset form after 3 seconds
      setTimeout(() => {
        setIsSubmitted(false);
        setFormData({ name: '', phone: '', email: '' });
      }, 3000);
    }, 1000);
  };

  return (
    <div className="app-container">
      <div className="glass-card">
        <div className="header">
          <h1 className="greeting">Good Morning!</h1>
          <p className="subtitle">Let's start the day with something great.</p>
        </div>

        <form onSubmit={handleSubmit} className="morning-form">
          <div className="form-group">
            <label htmlFor="name" className="form-label">Full Name</label>
            <input
              type="text"
              id="name"
              name="name"
              className="form-input"
              placeholder="Jeevan Marshal"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="phone" className="form-label">Phone Number</label>
            <input
              type="tel"
              id="phone"
              name="phone"
              className="form-input"
              placeholder="+91 98765 43210"
              value={formData.phone}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="email" className="form-label">Email Address</label>
            <input
              type="email"
              id="email"
              name="email"
              className="form-input"
              placeholder="yourmail@gmail.com"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <button
            type="submit"
            className="submit-btn"
            disabled={isSubmitting}
          >
            {isSubmitting ? 'Sending...' : 'Submit Details'}
          </button>
        </form>

        {isSubmitted && (
          <div className="success-message">
            Thank you! Your details have been received.
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
