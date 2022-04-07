if(self.main=='q'):
         for i in range(2):
            if(((self.qx-self.cx[i])**2 + (self.qy-self.cy[i])**2) < (self.cdamage**2) and self.can_col[i] != self.black):
                self.qhealth -= self.cdamage
                if(self.qhealth<=40 and self.qhealth>=30):
                    self.queen_col=self.lred
                elif(self.qhealth<=30 and self.qhealth>=20):
                    self.queen_col=self.blue
                elif(self.qhealth<=20 and self.qhealth>=10):
                    self.queen_col=self.lmag
                elif(self.qhealth<=10 and self.qhealth>=0):
                    self.queen_col=self.yellow   
                elif(self.qhealth<=0):
                    self.queen_col=self.black 
                    self.health=0

         if(self.qhealth < 0):
             self.running = 0 