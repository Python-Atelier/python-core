# 🐍 Control Flow - Questions

> **Master Python's decision-making and looping constructs!** 🔄

---

## 🏷️ **Question Categories**

- 🟢 **🟢 Basic** - Foundational concepts
- 🟡 **🟡 Intermediate** - Practical applications
- 🟠 **🟠 Advanced** - Complex scenarios
- 🔴 **🔴 Expert** - Real-world challenges

---

## 🟢 **Basic Level Questions** (1-6)

### Question 1: E-commerce Discount Calculator ⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Conditional Logic  
**📝 Skills Tested:** if/elif/else statements, business logic

**Task:** Create a discount calculator for different customer types based on purchase amounts.

**Real-life Scenario:** You're building an e-commerce website that offers different discounts:

- Regular customers: 5% off for purchases over $100, 10% off for purchases over $500
- VIP customers: 10% off for purchases over $50, 15% off for purchases over $200
- New customers: 3% off for purchases over $200

**Think about:**

- How do you handle different customer types and their specific rules?
- What happens when purchase amounts fall into different discount tiers?
- How do you ensure only one discount is applied?

**Challenge yourself:**

- Can you implement a loyalty points system that affects discount rates?
- What if you need to handle seasonal promotions on top of customer discounts?

**If you can't solve this, review:** Basic if/elif/else syntax, comparison operators, business logic

**💡 Pro Tip:** Always validate business rules and handle edge cases!

---

### Question 2: Weather App Decision System ⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** Boolean Logic  
**📝 Skills Tested:** and, or, not operators, weather logic

**Task:** Create a weather app that recommends activities based on temperature, humidity, and precipitation.

**Real-life Scenario:** Your weather app needs to suggest outdoor activities:

- Good for outdoor activities: temperature 15-30°C, humidity <70%, no rain
- Indoor activities recommended: temperature <10°C or >35°C, or humidity >80%, or rain
- Beach day: temperature >25°C, humidity <60%, no rain, sunny

**Think about:**

- How do you combine multiple weather conditions to make decisions?
- What happens when conditions are partially favorable?
- How do you prioritize recommendations when conditions conflict?

**Challenge yourself:**

- Can you implement a confidence score for each recommendation?
- What if you need to consider wind speed and UV index as well?

**If you can't solve this, review:** Logical operators, boolean expressions, operator precedence

**🌤️ Weather Logic:** Combine multiple conditions efficiently with logical operators!

---

### Question 3: Inventory Management System ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Loops & Iteration  
**📝 Skills Tested:** for loops, range function, inventory logic

**Task:** Create an inventory management system that tracks product stock levels and generates alerts.

**Real-life Scenario:** You're managing a warehouse inventory system:

- Track products with their current stock levels
- Generate low stock alerts (below 10 units)
- Calculate reorder quantities (restock to 50 units)
- Print inventory reports with status indicators

**Think about:**

- How do you process multiple products efficiently?
- What happens when you need to check each product's stock level?
- How do you generate different types of alerts based on stock levels?

**Challenge yourself:**

- Can you implement automatic reordering when stock reaches critical levels?
- What if you need to track products by category and generate category-specific reports?

**If you can't solve this, review:** for loop syntax, range() function, business logic implementation

**📦 Inventory Tip:** Use loops to process large datasets efficiently!

---

### Question 4: ATM Transaction System ⭐⭐

**⏱️ Time Estimate:** 18 minutes  
**🎯 Category:** Loops & Iteration  
**📝 Skills Tested:** while loops, transaction logic, input validation

**Task:** Create an ATM system that handles multiple transactions until the user chooses to exit.

**Real-life Scenario:** You're building an ATM interface:

- Display menu options (check balance, withdraw, deposit, exit)
- Handle multiple transactions in a session
- Validate account balance before withdrawals
- Keep track of transaction history
- Exit when user chooses to quit

**Think about:**

- How do you keep the system running until the user decides to stop?
- What happens when you need to validate each transaction?
- How do you handle different types of user inputs?

**Challenge yourself:**

- Can you implement a daily withdrawal limit?
- What if you need to handle multiple account types (savings, checking)?

**If you can't solve this, review:** while loop syntax, loop termination, input validation, transaction logic

**🏦 ATM Logic:** Always validate transactions and provide clear user feedback!

---

### Question 5: Restaurant Menu Display System ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Loop Patterns  
**📝 Skills Tested:** nested loops, menu formatting, data organization

**Task:** Create a restaurant menu display system that shows categories and items with prices.

**Real-life Scenario:** You're building a digital menu system for a restaurant:

- Display menu categories (Appetizers, Main Course, Desserts)
- Show items in each category with descriptions and prices
- Format the menu nicely with proper spacing
- Calculate total items and average price per category

**Think about:**

- How do you organize and display hierarchical data (categories and items)?
- What happens when you need to process items within each category?
- How do you calculate statistics while displaying the data?

**Challenge yourself:**

- Can you implement a search function that finds items across all categories?
- What if you need to highlight vegetarian or gluten-free options?

**If you can't solve this, review:** nested loops, loop variables, data formatting, menu logic

**🍽️ Menu Logic:** Use nested loops to organize and display hierarchical data!

---

### Question 6: Traffic Light Simulation ⭐⭐

**⏱️ Time Estimate:** 16 minutes  
**🎯 Category:** Loop Control  
**📝 Skills Tested:** break, continue statements, traffic simulation

**Task:** Create a traffic light simulation that cycles through colors and handles emergency vehicles.

**Real-life Scenario:** You're simulating a traffic light system:

- Cycle through Red (30s), Yellow (5s), Green (25s)
- Skip to Green immediately if emergency vehicle detected
- Skip Yellow phase if no vehicles waiting
- Handle system shutdown gracefully

**Think about:**

- How do you interrupt normal flow when special conditions occur?
- What happens when you need to skip certain phases?
- How do you handle emergency situations that override normal operation?

**Challenge yourself:**

- Can you implement multiple traffic lights that coordinate with each other?
- What if you need to handle different traffic patterns during rush hour?

**If you can't solve this, review:** break and continue syntax, loop control flow, simulation logic

**🚦 Traffic Logic:** Use break and continue for intelligent flow control!

---

## 🟡 **Intermediate Level Questions** (7-12)

### Question 7: Student Grade Management System ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Advanced Conditionals  
**📝 Skills Tested:** complex boolean expressions, grade calculations

**Task:** Create a comprehensive student grade management system with multiple criteria.

**Real-life Scenario:** You're building a school management system:

- Calculate final grades based on assignments (30%), midterm (30%), final (40%)
- Assign letter grades: A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
- Handle special cases: incomplete assignments, extra credit, attendance bonus
- Generate grade reports with recommendations

**What to do:**

- Use complex conditional logic for grade calculations
- Handle multiple grading criteria and weights
- Implement special case handling
- Generate detailed grade reports

**What NOT to do:**

- Don't use too many nested if statements
- Don't forget edge cases in grade calculations
- Don't make logic overly complex

**If you can't solve this, review:** boolean expressions, logical operators, conditional logic, grade calculations

**📊 Grading Logic:** Use clear, readable conditional expressions for complex business rules!

---

### Question 8: Online Banking Security System ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Security Logic  
**📝 Skills Tested:** nested conditionals, security validation

**Task:** Implement a banking security system that validates transactions based on multiple factors.

**Real-life Scenario:** You're building online banking security:

- Check account balance before transactions
- Validate transaction limits (daily, monthly)
- Verify user authentication and session validity
- Handle suspicious activity detection
- Implement fraud prevention measures

**What to do:**

- Use nested conditionals for security checks
- Implement multiple validation layers
- Handle security alerts and account locks
- Provide appropriate error messages

**What NOT to do:**

- Don't expose sensitive information in error messages
- Don't ignore security edge cases
- Don't make security logic too permissive

**If you can't solve this, review:** nested conditionals, security logic, validation techniques

**🔒 Security Logic:** Always validate multiple factors for financial transactions!

---

### Question 9: E-commerce Shopping Cart ⭐⭐⭐

**⏱️ Time Estimate:** 28 minutes  
**🎯 Category:** Shopping Logic  
**📝 Skills Tested:** complex loops, cart management

**Task:** Create a shopping cart system with product management and checkout process.

**Real-life Scenario:** You're building an e-commerce shopping cart:

- Add/remove products from cart
- Calculate subtotal, tax, and shipping
- Apply discounts and coupons
- Handle inventory checks during checkout
- Process payment validation

**What to do:**

- Use loops to manage cart items
- Implement product quantity validation
- Calculate totals with multiple factors
- Handle checkout process step by step

**What NOT to do:**

- Don't allow negative quantities
- Don't forget to check inventory
- Don't ignore payment validation

**If you can't solve this, review:** complex loops, cart management, business logic implementation

**🛒 Cart Logic:** Always validate inventory and calculate totals accurately!

---

### Question 10: Hospital Patient Management ⭐⭐⭐

**⏱️ Time Estimate:** 35 minutes  
**🎯 Category:** Healthcare Logic  
**📝 Skills Tested:** patient data processing, medical logic

**Task:** Create a patient management system that processes patient data and generates alerts.

**Real-life Scenario:** You're building a hospital management system:

- Process patient vital signs (temperature, blood pressure, heart rate)
- Generate alerts for abnormal readings
- Track patient medication schedules
- Handle emergency situations
- Generate patient reports

**What to do:**

- Use loops to process patient data
- Implement medical alert logic
- Handle emergency protocols
- Generate comprehensive reports

**What NOT to do:**

- Don't ignore critical medical alerts
- Don't forget to validate medical data
- Don't make medical decisions without proper validation

**If you can't solve this, review:** healthcare logic, data validation, alert systems

**🏥 Medical Logic:** Always prioritize patient safety in healthcare systems!

---

### Question 11: Restaurant Order Processing ⭐⭐⭐

**⏱️ Time Estimate:** 32 minutes  
**🎯 Category:** Order Management  
**📝 Skills Tested:** order processing, kitchen coordination

**Task:** Create a restaurant order processing system that manages orders from kitchen to delivery.

**Real-life Scenario:** You're building a restaurant order system:

- Process customer orders with multiple items
- Calculate preparation times based on dish complexity
- Coordinate kitchen staff assignments
- Handle order modifications and cancellations
- Track order status from kitchen to delivery

**What to do:**

- Use loops to process order items
- Implement kitchen timing logic
- Handle order modifications
- Track order status changes

**What NOT to do:**

- Don't lose order modifications
- Don't forget to update order status
- Don't ignore kitchen capacity limits

**If you can't solve this, review:** order processing, status tracking, business workflow

**🍕 Order Logic:** Track orders through the entire process from kitchen to delivery!

---

### Question 12: Library Book Management ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Library System  
**📝 Skills Tested:** book tracking, due date management

**Task:** Create a library management system that tracks books, borrowers, and due dates.

**Real-life Scenario:** You're building a library management system:

- Track book availability and location
- Manage borrower accounts and borrowing limits
- Calculate due dates and late fees
- Handle book reservations and holds
- Generate overdue notices

**What to do:**

- Use loops to process book transactions
- Implement due date calculations
- Handle late fee calculations
- Generate library reports

**What NOT to do:**

- Don't allow borrowing beyond limits
- Don't forget to calculate late fees
- Don't ignore book availability

**If you can't solve this, review:** library logic, date calculations, transaction management

**📚 Library Logic:** Always track books and manage due dates accurately!

---

## 🟠 **Advanced Level Questions** (13-18)

### Question 13: Airline Booking System ⭐⭐⭐⭐

**⏱️ Time Estimate:** 45 minutes  
**🎯 Category:** Booking Logic  
**📝 Skills Tested:** complex booking algorithms, seat management

**Task:** Create an airline booking system with seat selection and flight management.

**Real-life Scenario:** You're building an airline booking system:

- Display available seats on aircraft
- Handle seat selection and booking
- Calculate ticket prices based on class and demand
- Manage flight schedules and connections
- Handle booking modifications and cancellations

**What to do:**

- Use nested loops for seat management
- Implement dynamic pricing logic
- Handle booking conflicts
- Manage flight connections

**What NOT to do:**

- Don't double-book seats
- Don't ignore flight capacity
- Don't forget to handle cancellations

**If you can't solve this, review:** booking algorithms, seat management, dynamic pricing

**✈️ Booking Logic:** Always prevent double bookings and manage capacity!

---

### Question 14: Smart Home Automation ⭐⭐⭐⭐

**⏱️ Time Estimate:** 50 minutes  
**🎯 Category:** Automation Logic  
**📝 Skills Tested:** sensor data processing, automation rules

**Task:** Create a smart home automation system that controls devices based on sensor data.

**Real-life Scenario:** You're building a smart home system:

- Process sensor data (temperature, motion, light, humidity)
- Control devices (thermostat, lights, security system)
- Implement automation rules and schedules
- Handle energy optimization
- Manage device conflicts

**What to do:**

- Use loops to process sensor data
- Implement automation rule engine
- Handle device coordination
- Optimize energy usage

**What NOT to do:**

- Don't create conflicting device states
- Don't ignore sensor failures
- Don't forget energy optimization

**If you can't solve this, review:** automation logic, sensor processing, device coordination

**🏠 Smart Home Logic:** Coordinate devices intelligently and optimize energy usage!

---

### Question 15: Supply Chain Management ⭐⭐⭐⭐

**⏱️ Time Estimate:** 55 minutes  
**🎯 Category:** Supply Chain  
**📝 Skills Tested:** inventory optimization, demand forecasting

**Task:** Create a supply chain management system that optimizes inventory and demand.

**Real-life Scenario:** You're building a supply chain system:

- Track inventory across multiple warehouses
- Forecast demand based on historical data
- Optimize reorder points and quantities
- Handle supplier lead times and costs
- Manage cross-warehouse transfers

**What to do:**

- Use loops to process inventory data
- Implement demand forecasting algorithms
- Calculate optimal reorder points
- Handle supply chain disruptions

**What NOT to do:**

- Don't ignore supplier lead times
- Don't forget demand seasonality
- Don't overlook transportation costs

**If you can't solve this, review:** supply chain logic, demand forecasting, inventory optimization

**📦 Supply Chain Logic:** Balance inventory costs with service levels!

---

### Question 16: Financial Portfolio Management ⭐⭐⭐⭐

**⏱️ Time Estimate:** 60 minutes  
**🎯 Category:** Financial Logic  
**📝 Skills Tested:** portfolio optimization, risk management

**Task:** Create a financial portfolio management system with risk assessment and rebalancing.

**Real-life Scenario:** You're building a portfolio management system:

- Track multiple investment positions
- Calculate portfolio performance and risk metrics
- Implement rebalancing algorithms
- Handle market volatility and alerts
- Generate investment recommendations

**What to do:**

- Use loops to process portfolio data
- Implement risk calculation algorithms
- Handle portfolio rebalancing
- Generate investment reports

**What NOT to do:**

- Don't ignore risk management
- Don't forget transaction costs
- Don't overlook market conditions

**If you can't solve this, review:** financial algorithms, risk management, portfolio optimization

**💰 Portfolio Logic:** Always balance returns with risk management!

---

## 🔴 **Expert Level Questions** (17-20)

### Question 17: Autonomous Vehicle Navigation ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 90 minutes  
**🎯 Category:** Navigation Logic  
**📝 Skills Tested:** pathfinding algorithms, sensor fusion

**Task:** Create an autonomous vehicle navigation system with obstacle avoidance and route optimization.

**Real-life Scenario:** You're building an autonomous vehicle system:

- Process sensor data (cameras, lidar, radar)
- Implement pathfinding and obstacle avoidance
- Handle traffic rules and regulations
- Optimize routes for efficiency and safety
- Manage emergency situations

**What to do:**

- Use complex loops for sensor processing
- Implement pathfinding algorithms
- Handle real-time decision making
- Manage safety protocols

**What NOT to do:**

- Don't ignore safety protocols
- Don't forget traffic rules
- Don't overlook sensor failures

**If you can't solve this, review:** navigation algorithms, sensor fusion, safety systems

**🚗 Navigation Logic:** Safety first in autonomous vehicle systems!

---

### Question 18: Industrial Process Control ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 100 minutes  
**🎯 Category:** Process Control  
**📝 Skills Tested:** control algorithms, system optimization

**Task:** Create an industrial process control system that manages manufacturing operations.

**Real-life Scenario:** You're building an industrial control system:

- Monitor production line sensors and equipment
- Implement control algorithms for quality assurance
- Handle equipment maintenance scheduling
- Optimize production efficiency
- Manage safety shutdowns

**What to do:**

- Use loops to monitor process variables
- Implement control algorithms
- Handle equipment coordination
- Manage safety protocols

**What NOT to do:**

- Don't ignore safety protocols
- Don't forget quality control
- Don't overlook equipment maintenance

**If you can't solve this, review:** control algorithms, process optimization, safety systems

**🏭 Process Logic:** Maintain quality and safety in industrial processes!

---

### Question 19: Emergency Response System ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 120 minutes  
**🎯 Category:** Emergency Management  
**📝 Skills Tested:** emergency protocols, resource allocation

**Task:** Create an emergency response system that coordinates resources during crises.

**Real-life Scenario:** You're building an emergency response system:

- Process emergency calls and assess priority
- Coordinate response teams and resources
- Implement evacuation and safety protocols
- Handle communication and public alerts
- Manage resource allocation and logistics

**What to do:**

- Use loops to process emergency calls
- Implement priority-based response logic
- Handle resource coordination
- Manage communication protocols

**What NOT to do:**

- Don't ignore emergency priorities
- Don't forget resource limitations
- Don't overlook communication protocols

**If you can't solve this, review:** emergency protocols, resource management, crisis coordination

**🚨 Emergency Logic:** Prioritize safety and coordinate resources effectively!

---

### Question 20: Smart City Infrastructure ⭐⭐⭐⭐⭐

**⏱️ Time Estimate:** 150 minutes  
**🎯 Category:** City Management  
**📝 Skills Tested:** infrastructure optimization, urban planning

**Task:** Create a smart city management system that optimizes urban infrastructure and services.

**Real-life Scenario:** You're building a smart city system:

- Monitor traffic flow and optimize signals
- Manage energy distribution and consumption
- Handle waste management and recycling
- Coordinate public transportation
- Implement environmental monitoring

**What to do:**

- Use complex loops for infrastructure monitoring
- Implement optimization algorithms
- Handle service coordination
- Manage environmental impact

**What NOT to do:**

- Don't ignore environmental impact
- Don't forget service coordination
- Don't overlook infrastructure limitations

**If you can't solve this, review:** urban planning, infrastructure optimization, environmental management

**🏙️ City Logic:** Optimize infrastructure while maintaining quality of life!

---

## 🆕 **Additional Practice Questions** (21-30)

### Question 21: Modern Pattern Matching with Match/Case ⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Modern Python Features  
**📝 Skills Tested:** Pattern matching, structural matching

**Task:** Use Python 3.10+ pattern matching to handle different data structures and types.

**Real-life Scenario:** You're building a data processing API that receives various message formats:

- Handle JSON messages with different structures
- Process different data types (dict, list, tuple, custom objects)
- Extract specific fields based on message type
- Apply different processing logic for each pattern

**Think about:**

- How does pattern matching differ from traditional if/elif chains?
- When is pattern matching more readable than multiple if statements?
- How do you handle nested patterns and complex data structures?

**Challenge yourself:**

- Can you implement a message router that handles 10+ different message types?
- What if you need to match against custom classes with specific attributes?

**If you can't solve this, review:** Pattern matching syntax, structural matching, Python 3.10+ features

**🎯 Pattern Matching:** More readable than nested if/elif chains for complex data!

---

### Question 22: Enhanced F-strings with Expressions ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** String Formatting  
**📝 Skills Tested:** F-string expressions, Python 3.12+ features

**Task:** Use enhanced f-strings (PEP 701) to create dynamic string formatting with complex expressions.

**Real-life Scenario:** You're building a logging system that formats messages dynamically:

- Include calculated values directly in f-strings
- Use multi-line f-strings for complex formatting
- Handle quotes and special characters in expressions
- Create dynamic templates based on data types

**Think about:**

- How do enhanced f-strings improve code readability?
- When should you use f-strings vs other formatting methods?
- How do you handle complex expressions within f-strings?

**Challenge yourself:**

- Can you create a dynamic SQL query builder using f-strings?
- What if you need to format nested data structures?

**If you can't solve this, review:** F-string syntax, PEP 701, string formatting best practices

**💬 Enhanced F-strings:** Support any valid Python expression and multi-line formatting!

---

### Question 23: Walrus Operator in Control Flow ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Assignment Expressions  
**📝 Skills Tested:** Walrus operator, control flow optimization

**Task:** Use the walrus operator (:=) to optimize control flow and reduce code duplication.

**Real-life Scenario:** You're building a data validation system:

- Validate user input and use the result in conditions
- Process data streams and check conditions simultaneously
- Optimize loops by combining assignment and condition checking
- Handle API responses with immediate validation

**Think about:**

- When does the walrus operator make code more readable?
- How do you avoid overusing the walrus operator?
- What are the performance implications of using assignment expressions?

**Challenge yourself:**

- Can you refactor existing code to use the walrus operator effectively?
- What if you need to handle multiple walrus operations in one expression?

**If you can't solve this, review:** Assignment expressions, walrus operator syntax, control flow optimization

**🦦 Walrus Operator:** Combine assignment and condition checking for cleaner code!

---

### Question 24: Context Managers with Multiple Resources ⭐⭐⭐

**⏱️ Time Estimate:** 35 minutes  
**🎯 Category:** Resource Management  
**📝 Skills Tested:** Context managers, resource coordination

**Task:** Create context managers that handle multiple resources and coordinate their lifecycle.

**Real-life Scenario:** You're building a database transaction system:

- Manage database connections and transactions
- Handle file operations within database transactions
- Coordinate logging and monitoring resources
- Ensure proper cleanup of all resources

**Think about:**

- How do you ensure all resources are properly managed?
- What happens when one resource fails to initialize?
- How do you handle nested context managers?

**Challenge yourself:**

- Can you implement a distributed transaction coordinator?
- What if you need to handle resource dependencies?

**If you can't solve this, review:** Context managers, resource management, exception handling

**🔧 Resource Management:** Ensure proper cleanup with context managers!

---



## 🎯 **Updated Study Progress Summary**

### 📈 **Completion Status:**

- 🟢 **Basic Level:** 0/6 completed
- 🟡 **Intermediate Level:** 0/6 completed
- 🟠 **Advanced Level:** 0/5 completed
- 🔴 **Expert Level:** 0/3 completed
- 🆕 **Additional Practice:** 0/10 completed

### ⏱️ **Total Estimated Time:** 12 hours 15 minutes

### 🎓 **Next Steps:**

1. Start with Basic Level questions (1-6)
2. Move to Intermediate when comfortable
3. Challenge yourself with Advanced concepts
4. Master Expert level for real-world scenarios
5. Practice with Additional Questions (21-30) featuring modern Python features

---

> **💡 Pro Tip:** Modern Python features like pattern matching and enhanced f-strings make control flow more readable and powerful!

---

## 🆕 **Additional Practice Questions** (31-35)

### Question 31: Modern Pattern Matching with Match/Case ⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Modern Python Features  
**📝 Skills Tested:** Pattern matching, structural matching, Python 3.10+ features

**Task:** Use Python 3.10+ pattern matching to handle different data structures and types.

**Real-life Scenario:** You're building a data processing API that receives various message formats:
- Handle JSON messages with different structures
- Process different data types (dict, list, tuple, custom objects)
- Extract specific fields based on message type
- Apply different processing logic for each pattern

**Think about:**
- How does pattern matching differ from traditional if/elif chains?
- When is pattern matching more readable than multiple if statements?
- How do you handle nested patterns and complex data structures?

**Challenge yourself:**
- Can you implement a message router that handles 10+ different message types?
- What if you need to match against custom classes with specific attributes?

**If you can't solve this, review:** Pattern matching syntax, structural matching, Python 3.10+ features

**🎯 Pattern Matching:** More readable than nested if/elif chains for complex data!

---

### Question 32: Enhanced F-strings with Expressions ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** String Formatting  
**📝 Skills Tested:** F-string expressions, Python 3.12+ features

**Task:** Use enhanced f-strings (PEP 701) to create dynamic string formatting with complex expressions.

**Real-life Scenario:** You're building a logging system that formats messages dynamically:
- Include calculated values directly in f-strings
- Use multi-line f-strings for complex formatting
- Handle quotes and special characters in expressions
- Create dynamic templates based on data types

**Think about:**
- How do enhanced f-strings improve code readability?
- When should you use f-strings vs other formatting methods?
- How do you handle complex expressions within f-strings?

**Challenge yourself:**
- Can you create a dynamic SQL query builder using f-strings?
- What if you need to format nested data structures with complex expressions?

**If you can't solve this, review:** Enhanced f-strings, PEP 701, string formatting, complex expressions

**💬 Enhanced F-strings:** Support any valid Python expression and multi-line formatting!

---

### Question 33: Walrus Operator in Control Flow ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Assignment Expressions  
**📝 Skills Tested:** Walrus operator, control flow optimization

**Task:** Use the walrus operator (:=) to optimize control flow and reduce code duplication.

**Real-life Scenario:** You're building a data validation system:
- Validate user input and use the result in conditions
- Process data streams and check conditions simultaneously
- Optimize loops by combining assignment and condition checking
- Handle API responses with immediate validation

**Think about:**
- When does the walrus operator make code more readable?
- How do you avoid overusing the walrus operator?
- What are the performance implications of using assignment expressions?

**Challenge yourself:**
- Can you refactor existing code to use the walrus operator effectively?
- What if you need to handle multiple walrus operations in one expression?

**If you can't solve this, review:** Assignment expressions, walrus operator syntax, control flow optimization

**🦦 Walrus Operator:** Combine assignment and condition checking for cleaner code!

---

### Question 34: Context Managers with Multiple Resources ⭐⭐⭐

**⏱️ Time Estimate:** 35 minutes  
**🎯 Category:** Resource Management  
**📝 Skills Tested:** Context managers, resource coordination

**Task:** Create context managers that handle multiple resources and coordinate their lifecycle.

**Real-life Scenario:** You're building a database transaction system:
- Manage database connections and transactions
- Handle file operations within database transactions
- Coordinate logging and monitoring resources
- Ensure proper cleanup of all resources

**Think about:**
- How do you ensure all resources are properly managed?
- What happens when one resource fails to initialize?
- How do you handle nested context managers?

**Challenge yourself:**
- Can you implement a distributed transaction coordinator?
- What if you need to handle resource dependencies?

**If you can't solve this, review:** Context managers, resource management, exception handling

**🔧 Resource Management:** Ensure proper cleanup with context managers!

---

### Question 35: Generator Expressions and Memory Efficiency ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Memory Optimization  
**📝 Skills Tested:** Generator expressions, memory efficiency

**Task:** Use generator expressions to process large datasets efficiently without loading everything into memory.

**Real-life Scenario:** You're processing a large log file:
- Filter log entries based on criteria
- Transform data without storing intermediate results
- Calculate statistics on streaming data
- Handle data that's too large to fit in memory

**Think about:**
- When should you use generator expressions vs list comprehensions?
- How do generator expressions improve memory usage?
- What are the trade-offs between memory and performance?

**Challenge yourself:**
- Can you implement a streaming data processor?
- What if you need to process data from multiple sources?

**If you can't solve this, review:** Generator expressions, memory management, streaming data

**💾 Memory Efficiency:** Process large datasets without loading everything into memory!

---

## 🎯 **Updated Study Progress Summary**

### 📈 **Completion Status:**

- 🟢 **Basic Level:** 0/6 completed
- 🟡 **Intermediate Level:** 0/6 completed
- 🟠 **Advanced Level:** 0/5 completed
- 🔴 **Expert Level:** 0/3 completed
- 🆕 **Additional Practice:** 0/10 completed

### ⏱️ **Total Estimated Time:** 13 hours 45 minutes

### 🎓 **Next Steps:**

1. Start with Basic Level questions (1-6)
2. Move to Intermediate when comfortable
3. Challenge yourself with Advanced concepts
4. Master Expert level for real-world scenarios
5. Practice with Additional Questions (21-35) featuring modern Python features

---

> **💡 Pro Tip:** Modern Python features like pattern matching and enhanced f-strings make control flow more readable and powerful!

---

_Happy Learning! Remember, control flow is the backbone of all real-world applications! 🔄✨_

---
