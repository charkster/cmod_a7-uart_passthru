module uart_passthru
( input uart_txd_in,
  input io_tx,
  output uart_rxd_out,
  output io_rx
  );
  
  assign uart_rxd_out = io_tx;
  assign io_rx        = uart_txd_in;

endmodule
