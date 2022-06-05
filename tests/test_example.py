def test_example(driver):
    driver.get("http://192.168.31.140:8081/")
    assert "Your Store" == driver.title
