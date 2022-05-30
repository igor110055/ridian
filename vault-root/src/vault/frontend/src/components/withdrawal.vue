<template>
  <div id="app">
    <div class="assessment-container container">

<router-link :to="'/'" class="router_link">FTX Wallet   </router-link>

        <!-- <button class="mt-4">Pay With FTX Wallet</button>
         <button class="mt-4" style="margin-left:10px">Pay With Binance Wallet</button> -->
        <div class="row">
            <div class="col-md-6 form-box">
              
                        <div class="form-top">
                            <div class="form-top-left">
                                <h3 class="text-left">Withdrawal Confirmation FTX Wallet</h3>
                                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
                            </div>
                        </div>
                        <div class="form-bottom">
                            <div class="form-group">
                                <label for="">Address</label>
                                <input type="text" readonly  v-model="user.address" name="amount"  class="form-email form-control" id="amount" required>
                            </div>
                            <div class="form-group">
                                <label for=""> Asset type</label>
                                <select class="form-control"  v-model="user.coin">
                                    <!-- <option selected>ETHRIUM</option>
                                    <option>BTC</option> -->
                                    <option>MATIC</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="">Amount</label>
                                <input type="number"  v-model="user.amount" name="amount" placeholder="Amount" class="form-email form-control" id="amount" required>
                            </div>
                            
                            <button type="button"  @click="submit()" class="btn btn-next mt-3">withdraw</button>
                          <span
                style="
                  position: relative;
                  font-size: 18px;
                  top: 54px;
                  right: 93px;
                "
                >User Matic Balance ({{ balance }})</span>
              <br />
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
      balance:'',
      user: {
       
        amount:"",
        coin:"",
        address:'0x97533358e902A5A2fD48dec4085Fa9B3e274ad7B'
      },
    };
  },
      mounted() {
    const path = "http://127.0.0.1:5000/detail";
    axios
      .get(path)
      .then((response) => {
        this.balance = response.data.withdrawable_balance;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {

    submit: function () {
      const path = "http://127.0.0.1:5000/widthdraw";
      axios
        .post(path, {
           
        amount:this.user.amount,
        coin:this.user.coin,
        address:this.user.address
        })
        .then((response) => {
            this.user.amount =''
            this.user.coin=''
          alert(response.data.message);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
