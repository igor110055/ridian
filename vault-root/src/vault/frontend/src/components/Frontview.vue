<template>
  <div id="app">
    <div class="assessment-container container">

<router-link :to="'/ftx'" class="router_link">Pay With FTX Wallet   </router-link>

        <!-- <button class="mt-4">Pay With FTX Wallet</button>
         <button class="mt-4" style="margin-left:10px">Pay With Binance Wallet</button> -->
        <div class="row">
            <div class="col-md-6 form-box">
                <div v-show="show1">

                        <div class="form-top">
                            <div class="form-top-left">
                                <h3 class="text-left">Deposit Confirmation Binance Wallet</h3>
                                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
                            </div>
                        </div>
                        <div class="form-bottom">
                              <div class="form-group">
                                <label for="">Email</label>
                                <input type="email"  v-model="user.email" name="amount" placeholder="Email" class="form-email form-control" id="amount" required>
                            </div>
                          <!-- <div class="form-group">
                                <label for="">Api Key</label>
                                <input type="text"  v-model="user.api_key" name="amount" placeholder="Api Key" class="form-email form-control" id="amount" required>
                            </div>
                            <div class="form-group">
                                <label for="">Seceret Key</label>
                                <input type="text"  v-model="user.seceret_key" name="amount" placeholder="Seceret Key" class="form-email form-control" id="amount" required>
                            </div> -->
                            <div class="form-group">
                                <label for="">User Deposit Confirmation</label>
                                <select class="form-control"  v-model="user.coin">
                                    <option selected>ETHRIUM</option>
                                    <option>BTC</option>
                                    <option>MATIC</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="">Amount</label>
                                <input type="number"  v-model="user.amount" name="amount" placeholder="Amount" class="form-email form-control" id="amount" required>
                            </div>
                            
                            <button type="button"  @click="next()" class="btn btn-next mt-3">Next</button>
                        </div>   
                </div>
                         <div v-show="show">
                        <div class="form-top">
                            <div class="form-top-left">
                                <h3><span><i class="fa fa-calendar-check-o" aria-hidden="true"></i></span> Ridian Binance Wallet Address</h3>
                                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
                            </div>
                        </div>
                        <div class="form-bottom">
                            <div class="form-group">
                                <h5 class="text-center mt-2">Deposit Address!</h5>

                            </div>
                            <div class="form-group">
                                <img class="mx-auto d-block mt-4"
                               
                                src="../assets/qr-code.svg"
                                alt="" height="100%" width="20%" style="margin-left: 200px;">                            </div>
                            <div class="form-group">
                                <p class="text-center mt-4 text-primary">0x7aa2a5f3592963fe9e35bf419565a8a483dffe75
                                </p>
                            </div>
                           
                            
                            <button style="    margin-right: 12px;" type="button" class="btn btn-previous" @click="previous()">Previous</button>
                            <button type="submit" class="btn" @click="submit()">Submit</button>
                        </div>
                    </div>                 
            </div>
        </div>
    </div>
  </div>
</template>
<script>
 import axios from "axios";
 
export default {
  data() {
    return {
        show:false,

        show1:true,
      user: {
        api_key: "",
        seceret_key: "",
        amount:"",
        coin:"",
        email:''
      },
    };
  },
  methods: {
        previous : function()
      {
    this.show1= true,
    this.show= false
      },
      next : function()
      {
    this.show1= false,
    this.show= true
      },
    submit: function () {
      const path = "http://127.0.0.1:5000/dataentry";
      axios
        .post(path, {
           api_key: 'this.user.api_key',
        seceret_key: 'this.user.seceret_key',
        amount:'this.user.amount',
        coin:'this.user.coin',
        email:'this.user.email'
        })
        .then((response) => {
            this.user.amount =''
      this.user.coin=''
       this.user.email=''
          alert(response.data.message)
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
