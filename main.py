from views.Login import Login
 
def main():
    router = Login()
    while True:
        router = router.render()

main()